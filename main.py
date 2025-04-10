import os
from pyexpat.errors import messages
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr

load_dotenv(override=True)

openai = OpenAI()
MODEL = "gpt-4o-mini"

system_message = "You are a helpful math tutor"

# We define a function that creates a message list for the conversation,
# combining the system prompt, previous interactions and the new user input
# it takes as param a message and a history for past interactions
#it assumes history is a list of dicts, better for: Quick reuse in API calls, less transformation needed

def chat(message, history):
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]
    stream = openai.chat.completions.create(model=MODEL, messages=messages, stream=True,)

    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ""
        yield response

#gradio interface
gr.ChatInterface(fn=chat, type="messages").launch(inbrowser=True)


#Assumes history is a list of tuples, better for: Relational DBs, simplicity, structured logs
def chat(message, history):
    messages = [{"role": "system", "content": system_message}]
    for user_message, assistant_message in history:
        messages.append({"role": "user", "content": user_message})
        messages.append({"role": "assistant", "content": assistant_message})
    messages.append({"role": "user", "content": message})
    
    stream = openai.chat.completions.create(model=MODEL, messages=messages, stream=True)
    
    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ""
        yield response


