#this file descibes the nodes that will be used in graph
from intellegence.graph_state import Conversation,gpt_invoked
from intellegence.adv_model import ai
from utility.model import K2_reply
from utility.counter import messages_since_last_intel

async def k2_node(state: Conversation):
    convo = state["messages"]
    print (f"within node K2\n")
    reply: K2_reply = await ai.ainvoke({"input": convo})
    print (f"the reply of K2 is: \n{reply}")
    return {"messages": reply.reply, "K2": {
        "confidence_score": reply.confidence_score,
        "info_score": reply.info_score,
        "scam_detected": reply.scam_detected,
        "new_info_detected": reply.new_info_detected,
        "reason": reply.reason
    }}

async def router(state: Conversation):
    # based on the state of conversation decide whether to route to K2_node or extraction_node
    if (state["K2"]["scam_detected"] is True and state["K2"]["info_score"]>0.85 and
        state["K2"]["new_info_detected"] is False and messages_since_last_intel>=3):
        gpt_invoked = True
        return "extraction"
    else:
        return "k2"

async def extraction_node(state: Conversation):
    