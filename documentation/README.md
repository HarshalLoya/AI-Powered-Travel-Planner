## Step 1: Figuring Out the Task

I got an assignment to make an AI that chats with me to learn my travel details—like my budget, how long I’m staying, and where I’m going—then builds a trip plan. I used fake data for suggestions and wanted it to be nice if my answers weren’t clear.

---

## Step 2: Making a Plan

I made a simple plan:
- Decide what to ask myself (the user).
- Write instructions for the AI.
- Code a chatbot to talk to me and make my plan.
- Test it and share it on Gradio.

---

## Step 3: Starting to Code

I used Gradio to start building. I made a `state` dictionary for my answers and a `chatbot` function to ask questions. I added fake data like `{"Paris": {"art": ["Louvre"]}}`, but it broke with a “tuple” error.

---

## Step 4: Enhancing the Chatbot with History and Error Fixes

Gradio gave me an error (`AttributeError: 'tuple' object has no attribute 'get'`) because I sent too much stuff. I fixed it up:

- **Using Chat History and Instructions:** I switched to using the full chat history—what I said and the AI’s replies—plus a big instruction set (`SYSTEM_PROMPT`). In `stream_response`, I turn it into a list with a `SystemMessage` for instructions and `HumanMessage`/`AIMessage` for past chats. New messages get added, and the AI (Groq’s Llama) uses it all to reply, remembering my earlier stuff like budget.
- **Streaming Replies:** I set it to send answers bit by bit, so I see them grow in Gradio.
- **Fixing Problems:** I thought about errors:
  - **API Key Fails:** If the key doesn’t load, it tells me. I could add a “Fix my key!” message.
  - **Saving Chat Fails:** If `chat_history.csv` can’t save, I’d catch it with:
    ```python
    try:
        save_turn_to_csv(message, answer)
    except:
        print("Chat didn’t save, but I’ll keep going!")
    ```

Now, it’s a smooth chatbot that remembers and handles hiccups well!

---

## Step 5: Setting Up My Files

I organized my project like this:
```
travel-planner-ai/
├── chat_history.csv       # Saves my chats
├── LICENSE                # Legal stuff
├── README.md              # Quick guide
├── requirements.txt       # Tools like Gradio
├── app/
│   ├── main.py            # Chatbot code
│   ├── prompts.py         # AI instructions
├── documentation/
│   ├── prompts_explanation.md  # Why my instructions work
```
Fake data’s in `prompts.py` with `SYSTEM_PROMPT`. It’s neat and simple!

---

## Step 6: Writing Instructions for the AI

I wrote `SYSTEM_PROMPT` in `prompts.py` to tell the AI:
- Ask me about my trip nicely (budget, days, where, etc.).
- Suggest activities from fake data.
- Make a day-by-day plan with times.

---

## Step 7: Making Sure It Works

I checked my instructions—they’re awesome:
- Asks me for all trip details.
- Nudges me nicely if I skip stuff.
- Chats like a friend and remembers what I say.

---