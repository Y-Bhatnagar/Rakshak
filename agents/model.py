#LLM Models used by Rakshak

from langchain_azure_ai.chat_models import AzureAIChatCompletionsModel
from backend.config import Kimi_K2_endpoint,Kimi_K2_key,GPT_5_mini_endpoint,GPT_5_mini_key

#instantating the Moonshot AI Kimi K2 Thinking model for conversation
Kimi_K2_model = AzureAIChatCompletionsModel(
    endpoint=Kimi_K2_endpoint,
    credential=Kimi_K2_key,
    model="Kimi-K2-Thinking",
    temperature = 0.75)

#instantating the GPT-5-mini model for final output
GPT_5_model = AzureAIChatCompletionsModel(
    endpoint=GPT_5_mini_endpoint,
    credential=GPT_5_mini_key,
    model="gpt-5-mini",
    temperature = 0)