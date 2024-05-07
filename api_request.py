from import_key import client
from prompt import system_message, generate_prompt


with open('article.txt', 'r') as file:
    # Read the entire contents of the file into a string variable
    article = file.read()


completion = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": generate_prompt(article)}
    ]
)

print(completion.choices[0].message)
