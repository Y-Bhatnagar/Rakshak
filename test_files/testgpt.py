from langchain_core.messages import AnyMessage, HumanMessage, AIMessage
from typing import List

test_msg : List[AnyMessage] = [HumanMessage(content="Hello sir, this is SBI Fraud Control. We’ve detected an unauthorized UPI attempt of ₹48,500. If not verified in 10 minutes, your account will be blocked."),
                               AIMessage(content="What? I didn't make any transfer. Which account is this?"),
                               HumanMessage(content="The Pune Camp branch account ending XX21. To stop the block, I just need verbal confirmation of your first name and city of account opening."),
                               AIMessage(content="I'm nervous. The app isn't opening. Are you sure this is legitimate?"),
                               HumanMessage(content="Yes sir, this is a live fraud hold. Please confirm now or the restriction will auto-apply.")]

num_msg: int = 3

#scam_intent: True, extraction false