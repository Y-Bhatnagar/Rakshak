from fastapi import FastAPI, Depends, Header, HTTPException
from backend.config import API_KEY
from utility.model import RakshakRequest,SessionState,K2_reply,AgentReply,gpt_extraction_reply, guvi_final_call, gpt_extraction_state
from backend.state import check_language, update_state, add_reply, store_final_payload, update_completed_call, check_final_call
from utility.state_lock import get_lock
from intellegence.graph import intel
from utility.counter import msg_count
from utility.call_back_file import send_guvi_callback
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

#authentication of the Api Key to access service
def verify_api_key (x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

# instance of FastAPI
app = FastAPI()

#defining the path operation
@app.post("/rakshak_input", dependencies = [Depends(verify_api_key)])
async def receiver (payload: RakshakRequest):
    if check_final_call(payload.sessionId) is True:
        logging.warning(f"Session already completed | sessionId={payload.sessionId}")
        reply = AgentReply(
            status="success",
            reply="This session has already been completed. No further messages are being accepted."
        )
        return reply
    else:
        message = check_language(payload.metadata.language)
        #locking the state
        alock = get_lock(payload.sessionId)
        async with alock:
            #storing the incoming message to the memory and returning the conversation and langgraph object of conversation
            sessionState : SessionState = await update_state(payload.sessionId, payload.message)
            #sending the message to AI for the analysis
            msgs = sessionState.lang_obj
            count = msg_count (payload.sessionId)
            print (f"Messages since last intel extraction: {count}\n")
            obj : list = await intel(msgs, count)
            K2_obj: K2_reply = obj[0]
            print(f"\nK2_obj: {K2_obj}\n")
            updated_state: SessionState = await add_reply (payload.sessionId, K2_obj)
            print(f"\nupdate_state: {updated_state}")
            # devriving the message object from the updated state
            K2_reply_msg_obj = updated_state.messages[-1]
            print(f"\n K2_reply_msg_obj: {K2_reply_msg_obj}\n")
            if K2_obj:
                agent_reply=AgentReply(
                    status="success",
                    reply= K2_reply_msg_obj.text
                    )
            else:
                agent_reply=AgentReply(
                    status="failure",
                    reply="K2 was unable to process the message"
                    )
            
            #Hitting the final endpoint to get the final reply object
            if len (obj) ==2:
                extraction_obj: gpt_extraction_reply = obj[1]
                print (f"GPT Extraction Object: {extraction_obj}\n")
                final_extracted_intel = gpt_extraction_state(
                    bankAccounts= extraction_obj.bankAccounts,
                    upiIds= extraction_obj.upiIds,
                    phishingLinks= extraction_obj.phishingLinks,
                    phoneNumbers= extraction_obj.phoneNumbers,
                    suspiciousKeywords= extraction_obj.suspiciousKeywords
                )
                final_call_obj = guvi_final_call(
                    sessionId= payload.sessionId,
                    scamDetected= extraction_obj.scam_detected,
                    totalMessagesExchanged= len (updated_state.messages),
                    extractedIntelligence= final_extracted_intel,
                    agentNotes= extraction_obj.agentNotes
                    )
                #storing the final payload
                store_final_payload (payload.sessionId, final_call_obj)
                #Hitting the Guvi endpoint
                logging.info(f"Sending GUVI callback | sessionId={final_call_obj.sessionId}")
                success = await send_guvi_callback(final_call_obj)
                if success:
                    logging.info(f"GUVI callback successful | sessionId={final_call_obj.sessionId}")
                else:
                    logging.error(f"GUVI callback failed | sessionId={final_call_obj.sessionId}")
                stat = update_completed_call (payload.sessionId)
            return agent_reply
