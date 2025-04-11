import re
import openai
from dotenv import load_dotenv
import gradio as gr
from formatter import format_math, latex_expressions


load_dotenv(override=True)

MODEL = "gpt-4o-mini"

system_message = (
    "You are a helpful math tutor.\n"
    "Always respond in Markdown.\n"
    "For all mathematical explanations, use KaTeX for rendering.\n"
    "Use `$...$` for inline math (within sentences) and `$$...$$` for full-line display math (centered formulas).\n"
    "For example, if you encounter an expression like 'Addition: Two vectors ($\\vec{a} = (a_1, a_2)$) and ($\\vec{b} = (b_1, b_2)$)':\n"
    "The output should be rendered in KaTeX display math as:\n"
    "$$ \\vec{a} = (a_1, a_2) $$\n"
    "$$ \\vec{b} = (b_1, b_2) $$\n"
    "Always use proper LaTeX syntax when writing math, and ensure the formulas are rendered in KaTeX.\n"
    "For example:\n"
    "Row Matrix: A matrix with a single row $$ ( 1 \\times n ) $$.\n"
    "Column Matrix: A matrix with a single column $$ ( m \\times 1 ) $$.\n"
    "Square Matrix: A matrix where the number of rows is equal to the number of columns $$ ( n \\times n ) $$.\n"
    "Then we can rewrite our equations as:\n"
    "$$ a_1 \\Delta x + b_1 \\Delta y = 0 $$\n"
    "$$ a_2 \\Delta x + b_2 \\Delta y = 0 $$\n"
    "Step 3: Assume Non-zero Determinants\n"
    "If the determinant of the coefficients (the matrix formed by ($a_1, b_1$) and ($a_2, b_2$)) is not equal to zero, meaning we have a unique solution, we can conclude that the only solution to these two equations must be:\n"
)

def chat(message, history):
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]
    response = openai.chat.completions.create(model=MODEL, messages=messages)
    # print("history")
    # print(history)
    # print("message")
    
    return format_math(response.choices[0].message.content, latex_expressions)

 
gr.ChatInterface(fn=chat, type="messages").launch(inbrowser=True)



