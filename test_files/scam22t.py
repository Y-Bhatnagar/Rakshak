from langchain_core.messages import AnyMessage, HumanMessage, AIMessage
from typing import List

test_msg : List[AnyMessage] = [HumanMessage(content="Hello sir, this is SBI Security Desk. Your savings account shows suspicious activity and may be temporarily blocked today."),
                               AIMessage(content="Blocked? I used my account this morning without any issue. What suspicious activity?"),
                               HumanMessage(content="Multiple failed debit attempts were detected from a non-registered device. As per RBI compliance, verification is mandatory."),
                               AIMessage(content="You usually send messages from official numbers. Why is this coming on WhatsApp?"),
                               HumanMessage(content="Due to server outage SMS gateway is down. WhatsApp verification is temporarily enabled to avoid inconvenience. Please cooperate to prevent permanent suspension."),
                               AIMessage(content="Okay… what verification do you need?"),
                               HumanMessage(content="Kindly confirm if your account is linked with UPI and mobile number ending with 32."),
                               AIMessage(content="Yes UPI is linked. Mobile ends with 32."),
                               HumanMessage(content="Thank you. To secure your account, please share your UPI ID so we can whitelist it."),
                               AIMessage(content ="I'm in office right now. Is this urgent or can it wait till evening?"),
                               HumanMessage(content="Sir if verification is not completed within 15 minutes, debit freeze will be applied automatically and reversal will take 24–48 hours."),
                               AIMessage(content="Hmm. I've heard about scams like this. How do I know you’re genuine?"),
                               HumanMessage(content="You may verify. This number is used by our backend team only. Also, no OTP or password is being asked. Only UPI ID for safety mapping."),
                               AIMessage(content="My UPI is yash.personal@upi. Please check."),
                               HumanMessage(content="Yes, it is showing active. For final confirmation, a ₹1 test credit will be sent. Please confirm once received."),
                               AIMessage(content="I didn't receive anything. Are you sure you sent it?"),
                               HumanMessage(content="Apologies. Our outbound credit failed. Please send ₹1 manually to secure.sbi@upi so we can complete verification instantly."),
                               AIMessage(content="This UPI name doesn’t look like SBI. Why is it “secure.sbi”?"),
                               HumanMessage(content="Sir, backend security handles do not reflect public branding. Please do not delay, otherwise account will enter risk category."),
                               AIMessage(content="Can I just visit the branch tomorrow and sort it out?"),
                               HumanMessage(content="Branch process will take minimum 3 working days and charges may apply.\nThis is faster. Send ₹1 to secure.sbi@upi or share your account number so we can complete from our side."),
                               AIMessage(content="Final reminder sir. If verification is not completed now, your account linked with mobile 98XXXX3210 will be blocked.\nImmediate action required. Send ₹1 to secure.sbi@upi or confirm your account number.")]



num_msg: int = 3