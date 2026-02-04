#this file descibes the nodes that will be used in graph
from intellegence.graph_state import Conversation
from intellegence.adv_model import ai,extraction_ai
from utility.model import K2_reply, gpt_extraction_reply

gpt_invoked: bool = False
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

def router(state: Conversation):
    # based on the state of conversation decide whether to route to K2_node or extraction_node
    if (state["K2"]["scam_detected"] is True and state["K2"]["info_score"]>0.85 and
        state["K2"]["new_info_detected"] is False and state["msg_since_last_intel"]>=3):
        global gpt_invoked
        gpt_invoked = True
        return "extraction"
    else:
        return "END"

async def extraction_node(state: Conversation):
    #extracting actionable intelligence using the extraction model
    convo= state["messages"]
    print (f"\n within the extraction node\n")
    extracted_info : gpt_extraction_reply = await extraction_ai.ainvoke({"input": convo})
    print (f"the extraction reply is:\n {extracted_info}")
    return({"extraction": {
        "scam_detected": extracted_info.scam_detected,
        "bankAccounts": extracted_info.bankAccounts,
        "upiIds": extracted_info.upiIds,
        "phishingLinks": extracted_info.phishingLinks,
        "phoneNumbers": extracted_info.phoneNumbers,
        "suspiciousKeywords": extracted_info.suspiciousKeywords,
        "agentNotes": extracted_info.agentNotes
    }})