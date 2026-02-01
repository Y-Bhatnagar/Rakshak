#this file descibes the nodes that will be used in graph
from intellegence.graph_state import Conversation
#from intellegence.agents import con_agent
from intellegence.adv_model import ai
from utility.model import K2_reply

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

#Gpt node for extraction
#async def extraction_node(state: Conversation):