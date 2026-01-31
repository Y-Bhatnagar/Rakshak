import os
import getpass

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise RuntimeError("API_KEY is not found in environment variables")

#endpoint and key for the Kim K2 thinking model
if not os.getenv("KIMI_K2_ENDPOINT"):
    os.environ["KIMI_K2_ENDPOINT"] = getpass.getpass("Enter Kim K2 thinking model endpoint: ")
Kim_K2_endpoint = os.getenv("KIMI_K2_ENDPOINT")

if not os.getenv("PROJECT_KEY"):
    os.environ["PROJECT_KEY"] = getpass.getpass("Enter Kim K2 thinking modelkey: ")
Kim_K2_key = os.getenv("PROJECT_KEY")

#endpoint and key for the GPT-5-mini model
if not os.getenv("GPT_5_MINI_ENDPOINT"):
    os.environ["GPT_5_MINI_ENDPOINT"] = getpass.getpass("Enter GPT-5-mini model endpoint: ")
GPT_5_mini_endpoint = os.getenv("GPT_5_MINI_ENDPOINT")

if not os.getenv("PROJECT_KEY"):
    os.environ["PROJECT_KEY"] = getpass.getpass("Enter GPT-5-mini modelkey: ")
GPT_5_mini_key = os.getenv("PROJECT_KEY")