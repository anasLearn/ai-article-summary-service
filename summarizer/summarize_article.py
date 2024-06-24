import json

from dotenv import load_dotenv

from .openai_config import client, openai_model
from .prompt import system_message, generate_prompt

# Load variables from the .env file
load_dotenv()


def summarize_article(article: str):
    completion = client.chat.completions.create(
        model=openai_model,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": generate_prompt(article)}
        ]
    )

    return json.loads(completion.choices[0].message.content.replace("\n", ' '))
