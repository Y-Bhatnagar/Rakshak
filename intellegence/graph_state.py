from utility.model import K2_reply_state, extraction_reply_state
from langgraph.graph import MessagesState

#defining the state of graph
class Conversation (MessagesState):
    K2: K2_reply_state
    extraction: extraction_reply_state
    msg_since_last_intel: int
    gpt_invoked: bool = False