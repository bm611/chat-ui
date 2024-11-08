import os
import openai

client = openai.OpenAI(
    base_url="https://api.cerebras.ai/v1",
    api_key=os.environ.get("CEREBRAS_API_KEY"),
)


def get_chat_response(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3.1-70b",
    )
    response = chat_completion.choices[0].message.content
    return response
