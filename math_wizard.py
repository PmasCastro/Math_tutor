import ollama
import gradio as gr


MODEL = "llama3.2"

system_msg = (
    "You are a helpful math tutor.\n"
    "Always respond in Markdown.\n"
    "Use `$...$` for inline math (inside sentences).\n"
    "Use `$$...$$` for full-line display math (centered formulas).\n"
    "Use proper LaTeX syntax when writing math."
)

system_msg += "Only output rendered Latex"
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
    # print("HISTORY")
    # print(history)
    # print("MESSAGE")
    # print(message)
    response = ""
    for chunk in stream:
        content = chunk['message']['content'] or ""
        response += content
        yield response
        print(response)

# gradio interface

# view = gr.Blocks(
#     gr.ChatInterface(fn=chat_bot).launch(inbrowser=True),
#     gr.Markdown(latex_delimiters=True)
# )

# view.launch()

chat_ui = gr.ChatInterface(
    fn=chat_bot,
    title="📐 Math Tutor Chatbot",
)

# Launch with auto browser
chat_ui.launch(inbrowser=True)


