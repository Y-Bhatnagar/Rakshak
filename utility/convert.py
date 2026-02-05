from pydantic import BaseModel
from typing import Literal
from datetime import datetime
from langchain.messages import HumanMessage, AIMessage, AnyMessage
from utility.model import Message

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

#defining function to convert Langchain object back to message object
def convert_back(msg:AnyMessage):
    if isinstance(msg, HumanMessage):
        return Message(sender="scammer", text=msg.content, timestamp=datetime.now())
    elif isinstance(msg, AIMessage):
        return Message(sender="user", text=msg.content, timestamp=datetime.now())