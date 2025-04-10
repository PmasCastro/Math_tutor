import os
from pyexpat.errors import messages
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr

load_dotenv(override=True)

openai = OpenAI()
MODEL = "gpt-4o-mini"

system_msg = "You are a helpful math tutor"

# Define a function to create a message list for the conversation,
# combining the system prompt, previous interactions, and new user input.
# It accepts a message and a history of past interactions as parameters.
# Assumes history is a list of tuples, making it more suitable for:
# - Relational DBs
# - Simplicity
# - Structured logs
def chat(message, history):
    messages = [{"role": "system", "content": system_msg}]
    for user_msg, assistant_msg in history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": assistant_msg})
    messages.append({"role": "user", "content": message})
    
    stream = openai.chat.completions.create(model=MODEL, messages=messages, stream=True)
    
    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ""
        yield response

#gradio interface
gr.ChatInterface(fn=chat, type="messages").launch(inbrowser=True)


