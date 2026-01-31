from utility.convert import convert_obj
from utility.model import Message, SessionState

#internal memory state
sessionHist: dict [str, SessionState] = {}

#defining function to check the input language
def check_language(language: str):
    if language != "English":
        return "input language is not english"
    return "correct input language"

#defining the function to update the state and share the updated state
def update_state (sessionId:str, message: Message) -> SessionState:
    #converting the message to object
    lang_messg_obj = convert_obj(message)
    if sessionId not in sessionHist:
        sessionHist[sessionId] = SessionState(messages = [message], lang_obj=[lang_messg_obj])
    else:
        sessionHist[sessionId].messages.append(message)
        sessionHist[sessionId].lang_obj.append(lang_messg_obj)
    return sessionHist[sessionId]