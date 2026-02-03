#add checks guviCallbackSent: true

from fastapi import FastAPI, Depends, Header, HTTPException
from backend.config import API_KEY
from utility.model import RakshakRequest,SessionState,K2_reply,AgentReply
from backend.state import check_language, update_state, add_reply
from utility.state_lock import get_lock
from intellegence.graph import intel

#authentication of the Api Key to access service
def verify_api_key (x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

# instance of FastAPI
app = FastAPI()

#defining the path operation
@app.post("/rakshak_input", dependencies = [Depends(verify_api_key)])
async def receiver (payload: RakshakRequest):
    message = check_language(payload.metadata.language)
    #locking the state
    alock = get_lock(payload.sessionId)
    async with alock:
        #storing the incoming message to the memory and returning the conversation and langgraph object of conversation
        sessionState : SessionState = await update_state(payload.sessionId, payload.message)
        #sending the message to AI for the analysis
        msgs = sessionState.lang_obj
        K2_obj: K2_reply = await intel(msgs)
        updated_state: SessionState = await add_reply (payload.sessionId, K2_obj)
        # devriving the message object from the updated state
        K2_reply_msg_obj = updated_state.messages[-1]
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
        return agent_reply
        #on receiving final message hitting the last API
        