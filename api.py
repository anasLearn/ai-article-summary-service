import os

from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

from summarizer.summarize_article import summarize_article

load_dotenv()
app = FastAPI()
host = os.environ.get("HOST", "127.0.0.1")
port = int(os.environ.get("PORT", "5010"))


@app.get("/ping")
async def ping():
    return "Hello, I am alive"


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
    uvicorn.run("api:app", host=host, port=port, reload=True)
