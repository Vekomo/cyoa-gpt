import os
from dotenv import load_dotenv

import openai
from embedding import res

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_message_from_response(response):
    return response["choices"][0]["message"]

def get_user_input():
    return input("You: ")

def call_chat_api(chat):
    try:
        return openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat,
            temperature=0.6,
        )
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return None

def conversation_loop(chat):
    user_content = ""
    while True:
        user_content = get_user_input()
        if user_content == "END":
            break
        user_entry = {"role": "user", "content": user_content}
        chat.append(user_entry)
        
        response = call_chat_api(chat)
        if response is None:
            print("Unable to continue conversation due to API error.")
            break
        
        gpt_entry = get_message_from_response(response)
        
        print("ChatGPT: " + gpt_entry["content"])
        chat.append(gpt_entry)
        
    return chat

if __name__ == "__main__":
  print(res.keys())
  print(conversation_loop([]))
    
    
'''
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "As an AI language model, I do not have the ability to hang or experience emotions, but I am here to assist you with any questions or concerns you may have. How can I assist you today?",
        "role": "assistant"
      }
    }
  ],
  "created": 1684466911,
  "id": "chatcmpl-7Hl55CDnKcUI7gPtfeqlCeXokrqBZ",
  "model": "gpt-3.5-turbo-0301",
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 41,
    "prompt_tokens": 20,
    "total_tokens": 61
  }
}
'''
