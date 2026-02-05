from langgraph.graph import START, StateGraph, END
import asyncio
from langchain.messages import AnyMessage
from langgraph.checkpoint.memory import InMemorySaver
from intellegence.nodes import k2_node,router,extraction_node
from intellegence.graph_state import Conversation
from test_files.scam22t import test_msg,num_msg
from utility.model import K2_reply, gpt_extraction_reply
from typing import List

# graph state is being imported from another file

memory = InMemorySaver()

graph = StateGraph(Conversation)
graph.add_node("k2", k2_node)
graph.add_node("router", router)
graph.add_node("extraction", extraction_node)


graph.add_edge(START,"k2")
graph.add_edge("k2", "router")
graph.add_edge("extraction", END)

flow = graph.compile(checkpointer=memory)
config = {"configurable" : {"thread_id" : "1"}}
        
async def intel(test_msg: List[AnyMessage], num_msg: int):
    state = await flow.ainvoke({"messages": test_msg, "msg_since_last_intel": num_msg}, config=config)
    print(f"\nthe graph reply: {state}\n")
    if state.get("gpt_invoked") is False:
        last_reply = state["messages"][-1].content
        print(f"last_message: {last_reply}\n")
        K2_obj = K2_reply(
            reply= [state["messages"][-1]],
            confidence_score= state["K2"]["confidence_score"],
            info_score= state["K2"]["info_score"],
            scam_detected= state["K2"]["scam_detected"],
            new_info_detected= state["K2"]["new_info_detected"],
            reason= state["K2"]["reason"]
        )
        print (f"K2 Object: {K2_obj}")
        return [K2_obj]
    else:
        last_reply = state["messages"][-2].content
        print(f"last_message: {last_reply}\n")
        K2_obj = K2_reply(
            reply= [state["messages"][-2]],
            confidence_score= state["K2"]["confidence_score"],
            info_score= state["K2"]["info_score"],
            scam_detected= state["K2"]["scam_detected"],
            new_info_detected= state["K2"]["new_info_detected"],
            reason= state["K2"]["reason"]
        )
        print (f"K2 Object: {K2_obj}")
        extracted_info = gpt_extraction_reply(
            scam_detected= state["extraction"]["scam_detected"],
            bankAccounts= state["extraction"]["bankAccounts"],
            upiIds= state["extraction"]["upiIds"],
            phishingLinks= state["extraction"]["phishingLinks"],
            phoneNumbers= state["extraction"]["phoneNumbers"],
            suspiciousKeywords= state["extraction"]["suspiciousKeywords"],
            agentNotes= state["extraction"]["agentNotes"]
        )
        print (f"Extraction Object: {extracted_info}")
        return [K2_obj, extracted_info]