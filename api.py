from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

from summarize_article import summarize_article

app = FastAPI()


@app.get("/ping")
async def ping():
    return "Hello, I am alive"


class Article(BaseModel):
    text: str


@app.post("/summarize")
def predict(
    article: Article
):
    """
    Upload an article to the api and get a summary
    Args:
        article: A txt of an article

    Returns:

    """
    response_json = summarize_article(article.text)

    return response_json


if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8080)
