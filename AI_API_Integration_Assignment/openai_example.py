# =============================================================================
# 📌 AI API Integration - OpenAI
# Author: Kushal V R
# Description:
# This program sends user input to OpenAI GPT model and displays the response.
# Demonstrates API usage, environment variables, and error handling.
# =============================================================================

import os
from openai import OpenAI

# =============================================================================
# 🔐 API CONFIGURATION
# Load API key securely from environment variable
# =============================================================================
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise EnvironmentError(
        "OPENAI_API_KEY is not set.\n"
        "Set using: $env:OPENAI_API_KEY='your_key_here'"
    )

# Initialize OpenAI client
client = OpenAI(api_key=api_key)


# =============================================================================
# 🤖 FUNCTION: Query OpenAI API
# =============================================================================
def query_openai(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error: {str(e)}"


# =============================================================================
# ▶️ MAIN EXECUTION
# =============================================================================
if __name__ == "__main__":
    print("=" * 50)
    print("        OpenAI — AI Query Program")
    print("=" * 50)

    user_prompt = input("Enter your prompt: ").strip()

    if not user_prompt:
        print("No prompt entered.")
    else:
        print("\nQuerying OpenAI API...\n")
        result = query_openai(user_prompt)

        print("─" * 50)
        print("Response:")
        print("─" * 50)
        print(result)