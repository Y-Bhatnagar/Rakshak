#This file contains the pydantic models that are being used in the Rakshak app
from pydantic import BaseModel, Field, conlist
from typing import List, Optional, Literal, Annotated, TypedDict
from datetime import datetime
from langchain.messages import AnyMessage,AIMessage

#pydantic models defining the structure of incoming data in rakshak file
class Message(BaseModel):
    sender: Literal["scammer", "user"]
    text: str
    timestamp: datetime

class Metadata(BaseModel):
    channel: str
    language: str
    locale: str

class RakshakRequest(BaseModel):
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
    phoneNumbers: Optional[List[str]]
    suspiciousKeywords: Optional[List[str]]

class EngagementMetrics(BaseModel):
    engagementDurationSeconds: int
    totalMessagesExchanged: int

class Response(BaseModel):
    status: str
    scamDetected: str
    engagementMetrics: EngagementMetrics
    extractedIntelligence: ExtractedIntelligence
    agentNotes: str

#pydantic model for conversing agent reply to the endpoint
class AgentReply(BaseModel):
    status: str
    reply: str

#pydantic model for K2's reply
class K2_reply(BaseModel):
    reply: Annotated[List[AIMessage], Field(min_length=1,description="Human-like assistant reply to be sent to the user")]
    confidence_score: float = Field(ge=0.0, le=1.0, description="Confidence score for the K2 reply")
    info_score: float = Field(ge=0.0, le=1.0, description="Information score describes how sufficient the conversation is for extracting structured scammer intelligence (accounts, links, payment handles")
    scam_detected: bool = Field(description="Whether a scam was detected in the conversation")
    new_info_detected: bool = Field(description="set this as True if their is some new actionable intellegence in the last message that is not available in the rest of conversation")
    reason: str = Field(description="Reason for for considering the conversation as a scam or not")

class K2_reply_state(TypedDict):
    confidence_score: float
    info_score: float
    scam_detected: bool
    new_info_detected: bool
    reason: str

#pydantic model for storing K2 reply metadata in the state
class K2_metadata(BaseModel):
    confidence_score: float
    info_score: float
    scam_detected: bool
    new_info_detected: bool
    reason: str
    reply_number: int

#pydantic model for GPT extraction reply
class gpt_extraction_reply(BaseModel):
    scam_detected: bool = Field(description="Whether a scam was detected in the conversation")
    bankAccounts: List[str] = Field(default_factory=list,description="List of bank account numbers extracted from the conversation")
    upiIds: List[str] = Field(default_factory=list,description="List of UPI IDs extracted from the conversation")
    phishingLinks: List[str] = Field(default_factory=list,description="List of phishing links extracted from the conversation")
    phoneNumbers: List[str] = Field(default_factory=list,description="List of phone numbers extracted from the conversation")
    suspiciousKeywords: List[str] = Field(default_factory=list,description="List of suspicious keywords indicating scam intent in the conversation")
    agentNotes: str = Field(description="Brief reason explaining why the conversation is considered to have scam intent")