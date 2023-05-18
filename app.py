import os
from dotenv import load_dotenv

import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Hey, chatGPT. How's it hangin'?"}
            ],
        temperature=0.6,
    )
    print(response)

if __name__ == "__main__":
    main()
