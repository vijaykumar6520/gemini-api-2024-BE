import google.generativeai as genai
import os
import logging


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

def call_gemini(data):
    try:
        response = model.generate_content("Write a story about a AI and magic")
        print(response.text)

        return response.text
    except Exception as e:
        logging.error(f'error occurred while calling gemini {e}', exc_info=True, stack_info=True)