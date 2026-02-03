from langgraph.graph import START, StateGraph, END
from langchain_core.messages import AnyMessage, HumanMessage, AIMessage
from typing import List
import asyncio
from langgraph.checkpoint.memory import InMemorySaver
from intellegence.nodes import k2_node
from intellegence.graph_state import Conversation
from test_files.scam3t import test_msg
from utility.model import K2_reply

# graph state is being imported from another file

memory = InMemorySaver()
gpt_invoked: bool

graph = StateGraph(Conversation)
graph.add_node("k2", k2_node)

graph.add_edge(START,"k2")
graph.add_edge("k2", END)

flow = graph.compile(checkpointer=memory)
config = {"configurable" : {"thread_id" : "1"}}

#async def intel (msg_hist: list[AnyMessage]):
# state = flow.invoke({"messages": msg_hist}, config=config)
        #K2_obj = K2_reply(
        # reply= [state["messages"][-1]],
        # confidence_score= state["K2"]["confidence_score"],
        # info_score= state["K2"]["info_score"],
        # scam_detected= state["K2"]["scam_detected"],
        # new_info_detected= state["K2"]["new_info_detected"],
        # reason= state["K2"]["reason"]
        #)
        #if gpt_invoked is not True:
        #return K2_obj
        #else:
        


async def run():
    state = await flow.ainvoke({"messages": test_msg}, config=config)
    last_reply = state["messages"][-1].content
    print(f"the graph reply: {state}\n")
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
    return K2_obj

asyncio.run(run())