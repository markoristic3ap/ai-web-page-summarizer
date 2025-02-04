from website import Website
from openai import OpenAI
from llm import SUPPORTED_LLMS, LLMInterface

llmClient = LLMInterface(provider=SUPPORTED_LLMS.OPEN_AI)
# llmClient = LLMInterface(provider=SUPPORTED_LLMS.OLLAMA) 

system_prompt = "You are an assistant that analyzes the contents of a website \
and provides a short summary, ignoring text that might be navigation related. \
You should always answer on Serbian language"
def user_prompt_for(website):
    user_prompt = f"You are looking at a website titled {website.title}"
    user_prompt += "\nThe contents of this website is as follows; \
please provide a short summary of this website. \
If it includes news or announcements, then summarize these too.\n\n"
    user_prompt += website.text
    return user_prompt


def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(website)}
    ]


def summarize(url):
    website = Website(url)
    response =llmClient.chat(messages_for(website))
    print(response)

summarize("https://creativewin.net")