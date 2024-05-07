system_message = """
You are a journalist student who speaks multiple languages. You will help me by summarizing new articles I give you in several languages.
"""


def generate_prompt(article: str):
    prompt = f"""
    I will give you a news article. I want you to read it, and to summarize it in exactly 3 sentences. You will give me the sentences as bullet points.
    I want you to do the summary in 3 languages: Arabic, French, and English.
    
    Here is the article:
    {article}
    """

    return prompt