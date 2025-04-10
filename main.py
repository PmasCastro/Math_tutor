import os
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr

load_dotenv(override=True)

openai = OpenAI()
MODEL = "gpt-4o-mini"

system_message = "You are a helpful math tutor"

#We define a function that creates a message list for the conversation,
#combining the system prompt, previous interactions and the new user input
def chat(message, history):
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]
    
    print("History is: ")
    print(history)
    print("And message is: ")
    print(message)

    stream = openai.chat.completions.create(model=MODEL, messages=messages, stream=True)

    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ""
        yield response

#gradio interface
gr.ChatInterface(fn=chat, type="messages").launch()

