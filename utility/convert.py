from pydantic import BaseModel
from typing import Literal
from datetime import datetime
from langchain.messages import HumanMessage, AIMessage

#pydantic models defining the structure of incoming data
class Message(BaseModel):
    sender: Literal["scammer", "user"]
    text: str
    timestamp: datetime

#defining function to convert the message object to Langchain object
def convert_obj(message:Message):
    if message.sender == "scammer":
        return HumanMessage(content=message.text)
    elif message.sender == "user":
        return AIMessage(content=message.text)