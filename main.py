import  chainlit as cl
from agents import Runner
from my_agents.agents import Assisatnt_Agent
from my_config.config import model

@cl.on_chat_start
async def start_chat():
    await cl.Message(content="I'm your AI Assistant! How can I help you today? Sir").send()

@cl.on_message
async def handle_message(message: cl.Message):
    user_input = message.content

    response = Runner.run_sync(Assisatnt_Agent, user_input)

    await cl.Message(content=f"Sir yes sir: {response.final_output}").send()