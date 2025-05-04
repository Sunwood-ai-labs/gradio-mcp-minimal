import os
import gradio as gr

def letter_counter(text: str, letter: str) -> int:
    """
    Count the number of occurrences of a letter in a given text.

    Args:
        text (str): Text to search through.
        letter (str): Letter to count.

    Returns:
        int: How many times `letter` appears in `text`.
    """
    return text.lower().count(letter.lower())

# --- Components -----------------------------------------------------------
# 明示的に label を指定して API 名を関数引数と一致させることで、
# MCP 経由の JSON キー不一致（"text_1" 問題）を解消するよ ✨
text_input = gr.Textbox(
    label="text",
    placeholder="Enter text here"
)
letter_input = gr.Textbox(
    label="letter",
    placeholder="Enter a single letter",
    max_lines=1
)
count_output = gr.Number(label="count")

# --- Interface ------------------------------------------------------------
demo = gr.Interface(
    fn=letter_counter,
    inputs=[text_input, letter_input],
    outputs=count_output,
    title="Letter Counter (MCP demo)",
    description="![Header Image](https://github.com/user-attachments/assets/a48bdf11-baf1-4e6d-8f4f-10bc33a68551)\n\nEnter text & a letter – count occurrences. Launches with MCP automatically.",
    api_name="letter_counter"
)

if __name__ == "__main__":
    # mcp_server=True starts the SSE endpoint at /gradio_api/mcp/sse
    # server_name="0.0.0.0" で全ネットワークインターフェースにバインドし、別PCからアクセス可能にするよ！
    # PORT 環境変数があればそれを使い、無ければデフォルト 7860✨
    demo.launch(
        mcp_server=True,
        server_name="0.0.0.0",
        server_port=int(os.getenv("PORT", 7860)),
    )