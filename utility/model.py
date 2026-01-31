#This file contains the pydantic models that are being used in the Rakshak app
from pydantic import BaseModel
from typing import List, Optional, Literal
from datetime import datetime
from langchain.messages import AnyMessage

#pydantic models defining the structure of incoming data in rakshak file
class Message(BaseModel):
    sender: Literal["scammer", "user"]
    text: str
    timestamp: datetime

class Metadata(BaseModel):
    channel: str
    language: str
    locale: str

class Request(BaseModel):
    sessionId: str
    message: Message
    conversationHistory: List[Message]
    metadata: Metadata

#pydantic model for the dictionary in state file
class SessionState(BaseModel):
    messages: List[Message]
    lang_obj: List[AnyMessage]

#pydantic model for replying to API request
class ExtractedIntelligence(BaseModel):
    bankAccounts: Optional[List[str]]
    upiIds: Optional[List[str]]
    phishingLinks: Optional[List[str]]

class EngagementMetrics(BaseModel):
    engagementDurationSeconds: int
    totalMessagesExchanged: int

class AgentReply(BaseModel):
    sender: str
    text: str
    timestamp: datetime

class Response(BaseModel):
    status: str
    scamDetected: str
    agentReply: AgentReply
    engagementMetrics: EngagementMetrics
    extractedIntelligence: ExtractedIntelligence
    agentNotes: str