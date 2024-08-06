system_message = """
You are a journalist student who speaks multiple languages. 
You will help me by summarizing the articles I give you in several languages.
"""


def generate_prompt(article: str):
    prompt = f"""
    I will give you a news article. I want you to read it, and to summarize it in at most 3 sentences. 
    You will give me the sentences as bullet points.
    I want you to do the summary in 3 languages: Arabic, Finnish and English.
    
    When you want to make the summary in other languages (different from the language of the original article), 
    don't just translate the summary from the original language. But do get the summary in the target language by 
    reanalysing the original article. 
    
    give me the result as a json variable looking like this:
    {{
      "EN": ["first sentence", "second sentence", "third sentence"],
      "FR": ["first sentence", "second sentence", "third sentence"],
      "AR": ["first sentence", "second sentence", "third sentence"]
    }}
    
    Make the sentences simple.
    
    Give me only the JSON object, nothing more, nothing less.
    
    Here is the article:
    {article}
    """

    return prompt
