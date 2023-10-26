import openai
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key = API_KEY


def generate_response(prompt, user_input):
    messages = [{"role": "system", "content": prompt}]

    question = {'role': 'user', 'content': user_input}

    messages.append(question)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )

    try:
        answer = response['choices'][0]['message']['content'].replace('\n', '<br>')
    except:
        answer = 'Error in response'

    return answer
