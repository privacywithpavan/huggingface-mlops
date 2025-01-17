import gradio as gr
from transformers import pipeline

summarizer = pipeline(task="summarization")

def get_summary(text):
    output = summarizer(text)
    summary = output[0]["summary_text"]
    return summary

demo = gr.Interface(
    fn=get_summary,
    inputs="text",
    outputs="text",
)

demo.launch()
