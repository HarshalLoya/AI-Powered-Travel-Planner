import gradio as gr
# from typing import TypedDict, Annotated, List
# from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
# from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
import sys
print(sys.path)

from app.prompts import SYSTEM_PROMPT

load_dotenv(dotenv_path=".env")
GROQ_LLAMA_70B_VERSATILE_API_KEY = os.getenv("GROQ_LLAMA_70B_VERSATILE_API_KEY")
(
    print("SUCCESSFULLY FETCHED LLAMA API KEY")
    if GROQ_LLAMA_70B_VERSATILE_API_KEY is not None
    else print("ERROR IN FETCHING LLAMA API KEY")
)

llm = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=GROQ_LLAMA_70B_VERSATILE_API_KEY, temperature=0, streaming=True)

def stream_response(message, history):
    print(f"Input: {message}. History: {history}\n")

    history_lnagchain_format = []
    history_lnagchain_format.append(SystemMessage(content=SYSTEM_PROMPT))

    for human, ai in history:
        history_lnagchain_format.append(HumanMessage(content=human))
        history_lnagchain_format.append(AIMessage(content=ai))

    if message is not None:
        history_lnagchain_format.append(HumanMessage(content=message))
        partial_message = ""
        for response in llm.stream(history_lnagchain_format):
            partial_message += response.content
            yield partial_message

demo_iterface = gr.ChatInterface(stream_response, textbox=gr.Textbox(placeholder="Enter your message here..."), autoscroll=True, flagging_mode="manual", save_history=True)

demo_iterface.launch(share=True, debug=True)