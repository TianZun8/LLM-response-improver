import os
import openai
from google.generativeai import GenerativeModel
import anthropic
import requests
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)

openai.api_key = os.getenv("OPENAI_API_KEY")
gemini = GenerativeModel('gemini-1.5-pro-latest')
anthropic_client = anthropic.Client(api_key=os.getenv("ANTHROPIC_API_KEY"))

def validate_env_vars(*keys):
    for key in keys:
        if not os.getenv(key):
            raise EnvironmentError(f"Missing required environment variable: {key}")

validate_env_vars("OPENAI_API_KEY", "ANTHROPIC_API_KEY", "DEEPSEEK_API_KEY")

def improve_prompt_with_gpt4o(original_prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a prompt engineering expert. Improve this prompt to get better results from LLMs. Return only the improved prompt."},
                {"role": "user", "content": original_prompt}
            ]
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        logging.error(f"OpenAI GPT-4o error: {e}")
        raise

def improve_with_gemini(response, improved_prompt):
    try:
        prompt = f"""Improve this response for the prompt: '{improved_prompt}'. Consider accuracy, completeness, and clarity. Return only the improved response.
        Current response: {response}"""
        result = gemini.generate_content(prompt)
        return result.text.strip()
    except Exception as e:
        logging.error(f"Gemini error: {e}")
        raise

def improve_with_deepseek(response, improved_prompt):
    try:
        headers = {
            "Authorization": f"Bearer {os.getenv('DEEPSEEK_API_KEY')}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "r1",
            "messages": [{"role": "user", "content": f"Improve response for this prompt '{improved_prompt}':\n\n{response}"}]
        }
        api_response = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers=headers,
            json=data
        )
        result = api_response.json()
        return result.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
    except Exception as e:
        logging.error(f"DeepSeek error: {e}")
        raise

def improve_with_anthropic(response, improved_prompt):
    try:
        prompt = f"Prompt: {improved_prompt}\n\nCurrent response: {response}"
        result = anthropic_client.completions.create(
            model="claude-3-opus-20240229",
            max_tokens_to_sample=4000,
            prompt=anthropic.HUMAN_PROMPT + prompt + anthropic.AI_PROMPT
        )
        return result.completion.strip()
    except Exception as e:
        logging.error(f"Anthropic error: {e}")
        raise

def main():
    user_prompt = input("Enter your prompt: ").strip()
    if not user_prompt:
        print("Prompt cannot be empty!")
        return

    try:
        improved_prompt = improve_prompt_with_gpt4o(user_prompt)
        logging.info(f"Improved prompt: {improved_prompt}")

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": improved_prompt}]
        ).choices[0].message["content"].strip()

        response = improve_with_gemini(response, improved_prompt)
        response = improve_with_deepseek(response, improved_prompt)
        response = improve_with_anthropic(response, improved_prompt)

        print("\nFinal optimized response:")
        print("=" * 30)
        print(response)
        print("=" * 30)

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")

if __name__ == "__main__":
    main()
