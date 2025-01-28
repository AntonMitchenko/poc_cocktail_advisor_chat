import os
import openai
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

main_prompt = """You are a sophisticated cocktail recommendation assistant with extensive knowledge of classic and contemporary cocktails.
Using the user's input and our comprehensive database of available cocktails, provide tailored suggestions that include
the cocktail name, a brief description, key ingredients, and any relevant serving suggestions. Ensure your recommendations
are engaging, informative, and align with the user's preferences."""

def generate_response_with_rag(query, results):
    try:
        messages = [
            {"role": "system", "content": main_prompt},
            {"role": "user", "content": query},
            {"role": "assistant", "content": results['ingredients']},  # Optional if results need to be provided
        ]
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
        )
        # print(messages)
        return response.choices[0].message.content
        # time.sleep(0.1)  # Add a delay to avoid hitting the API too fast
    except openai.OpenAIError as e:
        print(f"An error occurred: {str(e)}")
        return "Sorry, can not help right now."


