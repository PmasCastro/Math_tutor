# formatter.py

import re

latex_expressions = [
    r"\\vec{x}",
    r"\\frac\{.*\}\{.*\}",
    r"\\sum\{.*\}",
    r"\\int\{.*\}",
    r"\\alpha",  # Add more symbols or LaTeX expressions here
]

def format_math(text, latex_expressions):
    """
    This function scans the LLM output for known LaTeX expressions and formats them using KaTeX.
    :param text: The LLM response text
    :param latex_expressions: A list of common LaTeX expressions to search for
    :return: The text with the appropriate LaTeX expressions formatted for KaTeX
    """
    # Iterate over all the LaTeX expressions in the list
    for expr in latex_expressions:
        # Escape special characters and construct a regex pattern for the LaTeX expression
        escaped_expr = re.escape(expr)  # Escape special regex characters in LaTeX expressions
        pattern = r"\b" + escaped_expr + r"\b"  # Ensure exact matching of the expression

        # Format with KaTeX (wrap it in $$...$$ for display math)
        text = re.sub(pattern, lambda m: f"$$ {m.group(0)} $$", text)

    return text