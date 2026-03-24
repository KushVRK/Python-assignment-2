# =============================================================================
# 📌 AI API Integration Assignment - Cohere API
# =============================================================================
# Description:
# This program connects to the Cohere API using an API key stored
# in environment variables (no manual input required).
#
# It takes user input, sends it to the Cohere model,
# and displays the generated response.
#
# API Key Handling:
# - NOT hardcoded
# - NOT asked from user
# - Loaded securely from environment variable
# =============================================================================


import os
import cohere


# =============================================================================
# 🔐 LOAD API KEY FROM ENVIRONMENT
# =============================================================================

api_key = os.getenv("COHERE_API_KEY")

if not api_key:
    print("❌ Error: COHERE_API_KEY not set in environment variables.")
    print("Set it using PowerShell before running the program.")
    exit()


# Initialize Cohere client
client = cohere.Client(api_key)

# Model name
MODEL_NAME = "command-r-plus-08-2024"


# =============================================================================
# 🚀 FUNCTION: QUERY COHERE
# =============================================================================

def query_cohere(prompt: str) -> str:
    try:
        response = client.chat(
            model=MODEL_NAME,
            message=prompt,
            preamble="You are a helpful AI assistant.",
            temperature=0.7,
            max_tokens=300
        )

        return response.text.strip()

    except Exception as e:
        return f"Error: {str(e)}"


# =============================================================================
# 🧪 MAIN PROGRAM
# =============================================================================

if __name__ == "__main__":

    print("=" * 50)
    print("        Cohere — AI Query Program")
    print("=" * 50)
    print(f"Model: {MODEL_NAME}\n")

    user_prompt = input("Enter your prompt: ").strip()

    if not user_prompt:
        print("No prompt entered. Exiting.")
    else:
        print("\nQuerying Cohere API...\n")

        result = query_cohere(user_prompt)

        print("─" * 50)
        print("Response:")
        print("─" * 50)
        print(result)
        print("─" * 50)