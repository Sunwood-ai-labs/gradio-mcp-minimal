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

demo = gr.Interface(
    fn=letter_counter,
    inputs=["text", "text"],
    outputs="number",
    title="Letter Counter (MCP demo)",
    description="Enter text & a letter – count occurrences. Launches with MCP automatically.",
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