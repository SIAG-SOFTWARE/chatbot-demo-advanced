from openai import OpenAI
from utils.config import OPENAI_API_KEY, MODEL, MAX_TOKENS

client = OpenAI(api_key=OPENAI_API_KEY)

async def generate_reply(history, message):
    messages = [{"role": "system", "content": "You are a helpful business assistant."}]

    for entry in history:
        messages.append({"role": "user", "content": entry["user"]})
        messages.append({"role": "assistant", "content": entry["bot"]})

    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        max_tokens=MAX_TOKENS
    )

    return response.choices[0].message.content
