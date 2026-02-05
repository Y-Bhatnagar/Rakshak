from utility.convert import convert_obj, convert_back
from utility.model import Message, SessionState,K2_reply,K2_reply_state, K2_metadata, guvi_final_call
from typing import List


#internal memory state
sessionHist: dict [str, SessionState] = {}
metaDataHist: dict [str, List[K2_reply_state]] = {}
completedCall: dict [str, bool] = {}
finalPayload: dict [str, guvi_final_call] = {}

#defining function to check the input language
def check_language(language: str):
    if language != "English":
        return "input language is not english"
    return "correct input language"

#defining the function to update the state and share the updated state
async def update_state (sessionId:str, message: Message) -> SessionState:
    #converting the message to object
    lang_messg_obj = convert_obj(message)
    if sessionId not in sessionHist:
        sessionHist[sessionId] = SessionState(messages = [message], lang_obj=[lang_messg_obj])
    else:
        sessionHist[sessionId].messages.append(message)
        sessionHist[sessionId].lang_obj.append(lang_messg_obj)
    return sessionHist[sessionId]

#defining function to add K2 reply to the session state
async def add_reply(sessionId: str, obj:K2_reply):
    ai_msg = obj.reply
    msg : Message = convert_back(ai_msg[0])
    print (f"\n for ai_msg {ai_msg} \n converted message is {msg}\n")
    sessionHist[sessionId].messages.append(msg)
    sessionHist[sessionId].lang_obj.append(ai_msg)
    if sessionId not in metaDataHist:
        metaDataHist[sessionId] = []
        count = 1
    else:
        count = len(metaDataHist[sessionId]) + 1
    stateMetaData = K2_metadata(
        confidence_score = obj.confidence_score,
        info_score = obj.info_score,
        scam_detected = obj.scam_detected,
        new_info_detected = obj.new_info_detected,
        reason = obj.reason,
        reply_number = count
    )
    metaDataHist[sessionId].append(stateMetaData)
    return sessionHist[sessionId]

#function to update the completed call status
def update_completed_call(sessionId: str):
    completedCall[sessionId] = True
    sessionHist.pop(sessionId, None)
    metaDataHist.pop(sessionId, None)
    return "success"

#function to stor the final payload
def store_final_payload(sessionId: str, final_call_obj: guvi_final_call):
    finalPayload[sessionId] = final_call_obj
    return finalPayload[sessionId]

#function to check if final call is made for a session
def check_final_call(sessionId: str):
    if sessionId in finalPayload:
        return True
    return False