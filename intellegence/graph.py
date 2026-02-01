from langgraph.graph import START, StateGraph, MessagesState, END
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage, AnyMessage
from langgraph.checkpoint.memory import InMemorySaver
from intellegence.nodes import k2_node
from utility.model import K2_reply_state

#defining the state of graph
class Conversation (MessagesState):
    K2: K2_reply_state

memory = InMemorySaver()

graph = StateGraph(Conversation)
graph.add_node("k2", k2_node)

graph.add_edge(START,"k2")
graph.add_edge("k2", END)

flow = graph.compile(checkpointer=memory)
config = {"configurable" : {"thread_id" : "1"}}

#async def intel (msg_hist: list[AnyMessage]):
    #return flow.invoke({"messages": msg_hist}, config=config)"

async def run(msg_hist: list[AnyMessage]):
    return await flow.ainvoke({"messages": msg_hist}, config=config)