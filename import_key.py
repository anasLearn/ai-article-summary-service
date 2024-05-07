import os
from dotenv import load_dotenv

from openai import OpenAI

# Load variables from the .env file
load_dotenv()


# client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY"),
)
