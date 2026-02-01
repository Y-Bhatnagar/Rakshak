from langgraph.graph import START, StateGraph, END
from langchain_core.messages import AnyMessage, HumanMessage, AIMessage
from typing import List
import asyncio
from langgraph.checkpoint.memory import InMemorySaver
from intellegence.nodes import k2_node
from intellegence.graph_state import Conversation
from test_files.scam3t import test_msg

# graph state is being imported from another file

memory = InMemorySaver()

graph = StateGraph(Conversation)
graph.add_node("k2", k2_node)

graph.add_edge(START,"k2")
graph.add_edge("k2", END)

flow = graph.compile(checkpointer=memory)
config = {"configurable" : {"thread_id" : "1"}}

#async def intel (msg_hist: list[AnyMessage]):
    #return flow.invoke({"messages": msg_hist}, config=config)"

async def run():
    reply = await flow.ainvoke({"messages": test_msg}, config=config)
    print(f"Reply: {reply}")
    return reply

asyncio.run(run())