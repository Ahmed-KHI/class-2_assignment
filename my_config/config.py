from decouple import config
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel

my_key = config("GEMINI_API_KEY")
if not my_key or not isinstance(my_key, str):
    raise ValueError("GEMINI_API_KEY environment variable must be set to a valid string")
client = AsyncOpenAI(api_key=my_key,base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
model = OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=client)