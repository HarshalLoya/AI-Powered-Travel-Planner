import gradio as gr
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_groq import ChatGroq
import os
import csv
from datetime import datetime
import uuid
from dotenv import load_dotenv
from app.prompts import SYSTEM_PROMPT

CHATID = uuid.uuid4()
print(f"Chat/Session ID: {CHATID}")

load_dotenv(dotenv_path=".env")
GROQ_LLAMA_70B_VERSATILE_API_KEY = os.getenv("GROQ_LLAMA_70B_VERSATILE_API_KEY")
(
    print("SUCCESSFULLY FETCHED LLAMA API KEY")
    if GROQ_LLAMA_70B_VERSATILE_API_KEY is not None
    else print("ERROR IN FETCHING LLAMA API KEY")
)

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=GROQ_LLAMA_70B_VERSATILE_API_KEY,
    temperature=0,
    streaming=True,
)


def save_turn_to_csv(user_message, ai_message, file_path="chat_history.csv"):
    file_exists = os.path.exists(file_path)

    with open(file_path, mode="a", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(
            csv_file, fieldnames=["chat_id", "user_message", "ai_message", "timestamp"]
        )
        if not file_exists:
            writer.writeheader()
        writer.writerow(
            {
                "chat_id": CHATID,
                "user_message": user_message,
                "ai_message": ai_message,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        )


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
        
        try:    
            save_turn_to_csv(message, partial_message)
        except:
            print("Failed to save to csv, but continuing anyway!")


demo_iterface = gr.ChatInterface(
    stream_response,
    textbox=gr.Textbox(
        placeholder="Enter your message here...",
        container=False,
        autoscroll=True,
        scale=7,
    ),
    title="Travel Itinerary Planner",
)

demo_iterface.launch(share=True, debug=True)
