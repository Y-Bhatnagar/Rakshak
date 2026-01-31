import os
import getpass

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise RuntimeError("API_KEY is not found in environment variables")

#endpoint and key for the Kim K2 thinking model
if not os.getenv("Kim_K2_endpoint"):
    os.environ["Kim_K2_endpoint"] = getpass.getpass("Enter Kim K2 thinking model endpoint: ")
Kim_K2_endpoint = os.getenv("Kim_K2_endpoint")

if not os.getenv("Kim_K2_key"):
    os.environ["Kim_K2_key"] = getpass.getpass("Enter Kim K2 thinking modelkey: ")
Kim_K2_key = os.getenv("Kim_K2_key")

#endpoint and key for the GPT-5-mini model
if not os.getenv("GPT_5_mini_endpoint"):
    os.environ["GPT_5_mini_endpoint"] = getpass.getpass("Enter GPT-5-mini model endpoint: ")
GPT_5_mini_endpoint = os.getenv("GPT_5_mini_endpoint")

if not os.getenv("GPT_5_mini_key"):
    os.environ["GPT_5_mini_key"] = getpass.getpass("Enter GPT-5-mini modelkey: ")
GPT_5_mini_key = os.getenv("GPT_5_mini_key")