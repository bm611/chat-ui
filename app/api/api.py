import os
import openai
from typing import List, Tuple

client = openai.OpenAI(
    base_url="https://api.cerebras.ai/v1",
    api_key=os.environ.get("CEREBRAS_API_KEY"),
)


def get_chat_response(prompt: str, chat_history: List[Tuple[str, str]] = None):
    # Convert chat history into messages format
    messages = []

    # Add previous conversation context if exists
    if chat_history:
        for user_msg, assistant_msg in chat_history:
            messages.append({"role": "user", "content": user_msg})
            messages.append({"role": "assistant", "content": assistant_msg})

    # Add the current prompt
    messages.append({"role": "user", "content": prompt})

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama3.1-8b",
    )
    response = chat_completion.choices[0].message.content
    return response
