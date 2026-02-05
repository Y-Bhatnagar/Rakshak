from langchain_core.messages import AnyMessage, HumanMessage, AIMessage
from typing import List

test_msg : List[AnyMessage] = [HumanMessage(content="Hello sir, this is SBI Security Desk. Your savings account shows suspicious activity and may be temporarily blocked today."),
                               AIMessage(content="Blocked? I used my account this morning without any issue. What suspicious activity?"),
                               HumanMessage(content="Multiple failed debit attempts were detected from a non-registered device. As per RBI compliance, verification is mandatory."),
                               AIMessage(content="You usually send messages from official numbers. Why is this coming on WhatsApp?"),
                               HumanMessage(content="Due to server outage SMS gateway is down. WhatsApp verification is temporarily enabled to avoid inconvenience. Please cooperate to prevent permanent suspension."),
                               AIMessage(content="Okay… what verification do you need?"),
                               HumanMessage(content="Kindly confirm if your account is linked with UPI and mobile number ending with 32.")]
num_msg: int = 2