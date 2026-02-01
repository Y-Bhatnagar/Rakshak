from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langchain.messages import SystemMessage
from intellegence.model import Kimi_K2_model
from utility.model import K2_reply
from intellegence.system_prompts import K2_prompt

#conversing model
con_agent = create_agent(
    model = Kimi_K2_model,
    system_prompt = SystemMessage(content = K2_prompt),
    response_format = ToolStrategy(K2_reply)
)