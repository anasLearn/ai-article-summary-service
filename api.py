import os

from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

from summarizer.summarize_article import summarize_article

load_dotenv()
app = FastAPI()
HOST = os.environ.get("HOST", "localhost")
PORT = int(os.environ.get("PORT", "5010"))


@app.get("/ping")
async def ping():
    """
    GET /ping

    Health check endpoint to verify that the AI Summary service is alive.

    Returns:
        str: A confirmation message indicating the service is alive.
    """
    return "Hello, AI Summary service is alive"


class Article(BaseModel):
    text: str


@app.post("/summarize")
def predict(article: Article):
    """
    Upload an article to the api and get a summary
    Args:
        article: A txt of an article

    Returns:

    """
    response_json = summarize_article(article.text)

    for lang in response_json:
        sentences = response_json[lang]
        for i in range(len(sentences)):
            sentences[i] = sentences[i].encode("utf-8")

    return response_json


if __name__ == "__main__":
    uvicorn.run("api:app", host=HOST, port=PORT, reload=True)
