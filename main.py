import os
import openai
from dotenv import load_dotenv
import gradio as gr
from openai import OpenAI

load_dotenv(override=True)

MODEL = "gpt-4o-mini"

system_msg = "You are a helpful math tutor that specializes in proof-based Linear Algebra"

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

    print("Here's the history: ")
    print(history)
    print("Here's the messages: ")
    print(messages)
    
    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ""
        yield response
    
# gradio interface
gr.ChatInterface(fn=chat).launch(inbrowser=True)


