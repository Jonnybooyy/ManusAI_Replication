import gradio as gr
import pandas as pd

# Define the Gradio interface
iface = gr.Interface(
    fn=lambda text: text.upper(),
    inputs=gr.inputs.Textbox(lines=2, placeholder="Enter text here..."),
    outputs="text",
    title="Text Uppercaser",
    description="Enter text and see it converted to uppercase.",
)

# Launch the interface
if __name__ == "__main__":
    iface.launch()
