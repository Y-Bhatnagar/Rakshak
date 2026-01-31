#add checks guviCallbackSent: true

from fastapi import FastAPI, Depends, Header, HTTPException
from backend.config import API_KEY
from utility.model import Request,SessionState
from backend.state import check_language, update_state
from utility.state_lock import get_lock

#authentication of the Api Key to access service
def verify_api_key (x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

# instance of FastAPI
app = FastAPI()

#defining the path operation
@app.post("/rakshak_input", dependencies = [Depends(verify_api_key)])
async def receiver (payload: Request):
    message = check_language(payload.metadata.language)
    #locking the state
    alock = get_lock(payload.sessionId)
    async with alock:
        #storing the incoming message to the memory and returning the conversation and langgraph object of conversation
        sessionState : SessionState = update_state(payload.sessionId, payload.message)
        #sending the message to AI for the analysis
        #receive the response from AI and return it
        #on receiving final message hitting the last API
        