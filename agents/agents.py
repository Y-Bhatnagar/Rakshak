from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langchain.messages import SystemMessage
from agents.model import Kimi_K2_model
from utility.model import K2_reply

#conversing model
con_agent = create_agent(
    model = Kimi_K2_model,
    system_prompt = SystemMessage(content = K2_prompt),
    response_format = ToolStrategy(K2_reply)
)