import os
import ollama
import gradio as gr

MODEL = "llama3.2"

system_msg = (
    "You are a helpful advanced math tutor. "
    "Always display mathematical notation using '\\displaystyle' "
    "and ensure that the formatting looks clean and professional. "
    "Never display raw LaTeX notation, and ensure that all mathematical "
    "expressions are rendered in proper display style."
)
           
# Define a function to create a message list for the conversation,
# combining the system prompt, previous interactions, and new user input.
# It accepts a message and a history of past interactions as parameters.
# Assumes history is a list of tuples, making it more suitable for:
# - Relational DBs
# - Simplicity
# - Structured logs

def chat_bot(message, history):
    messages = [{"role": "system", "content": system_msg}]
    for user_msg, assistant_msg in history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": assistant_msg})
    messages.append({"role": "user", "content": message})
    
    stream = ollama.chat(model=MODEL, messages=messages, stream=True)
    
    response = ""
    for chunk in stream:
        content = chunk['message']['content'] or ""
        response += content
        yield response

# gradio interface
gr.ChatInterface(fn=chat_bot).launch(inbrowser=True)



