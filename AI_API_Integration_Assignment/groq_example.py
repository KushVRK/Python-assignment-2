# =============================================================================
# 📌 AI API Integration Assignment - Groq (LLaMA Model)
# Author: Kushal V R
#
# Description:
# This program integrates the Groq API using LLaMA models.
# It accepts user input, sends it to the Groq API, and displays the response.
#
# Features:
# - Secure API key handling using environment variables
# - Error handling
# - Clean user interaction
# =============================================================================

import os
from groq import Groq

# =============================================================================
# 🔐 API CONFIGURATION
# Load API key from environment variable
# =============================================================================
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise EnvironmentError(
        "GROQ_API_KEY is not set.\n"
        "Set it using: $env:GROQ_API_KEY='your_key_here'"
    )

# Initialize Groq client
client = Groq(api_key=api_key)


# =============================================================================
# 🤖 FUNCTION: query_groq
# Sends user prompt to Groq API and returns response
# =============================================================================
def query_groq(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=500,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error communicating with Groq API: {str(e)}"


# =============================================================================
# ▶️ MAIN EXECUTION
# =============================================================================
if __name__ == "__main__":
    print("=" * 50)
    print("       Groq LLaMA — AI Query Program")
    print("=" * 50)

    user_prompt = input("Enter your prompt: ").strip()

    if not user_prompt:
        print("No prompt entered.")
    else:
        print("\nQuerying Groq API...\n")
        result = query_groq(user_prompt)

        print("─" * 50)
        print("Response:")
        print("─" * 50)
        print(result)