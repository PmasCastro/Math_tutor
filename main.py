# import os
# import openai
# from dotenv import load_dotenv
# import gradio as gr

# load_dotenv(override=True)

# MODEL = "gpt-4o-mini"

# system_msg = (
#     "You are a helpful math tutor specializing in proof-based Linear Algebra. "
#     "All mathematical equations must be displayed using 'displaystyle'"
#     "You never show raw LaTeX and always give mathematical notation in text book style"
    
# )
           
# # Define a function to create a message list for the conversation,
# # combining the system prompt, previous interactions, and new user input.
# # It accepts a message and a history of past interactions as parameters.
# # Assumes history is a list of tuples, making it more suitable for:
# # - Relational DBs
# # - Simplicity
# # - Structured logs

# def chat(message, history):
#     messages = [{"role": "system", "content": system_msg}]
#     for user_msg, assistant_msg in history:
#         messages.append({"role": "user", "content": user_msg})
#         messages.append({"role": "assistant", "content": assistant_msg})
#     messages.append({"role": "user", "content": message})
    
#     stream = openai.chat.completions.create(model=MODEL, messages=messages, stream=True)
    
#     response = ""
#     for chunk in stream:
#         content = chunk.choices[0].delta.content or ""
#         response += content
#         yield "", history + [(message, response)]
    
# # gradio interface
# # gr.ChatInterface(fn=chat).launch(inbrowser=True)

# with gr.Blocks() as demo:
#     chatbot = gr.Chatbot(render_markdown=True)
#     msg = gr.Textbox(label="Your message")

#     chat_history = gr.State([])

#     msg.submit(fn=chat, inputs=[msg, chat_history], outputs=[msg, chatbot])

# demo.launch(inbrowser=True)