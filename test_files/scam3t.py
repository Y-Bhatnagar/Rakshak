from langchain_core.messages import AnyMessage, HumanMessage, AIMessage
from typing import List

test_msg : List[AnyMessage] = [HumanMessage(content="Hello sir, this is Rajesh calling from ABC Bank’s fraud prevention team. We’ve detected a suspicious transaction on your account this morning."),
                               AIMessage(content="Oh? What kind of transaction?"),
                               HumanMessage(content="An online transfer of ₹9,850 attempted from an unknown device. We immediately put it on hold for your safety.")]

#scam_intent: True, extraction false