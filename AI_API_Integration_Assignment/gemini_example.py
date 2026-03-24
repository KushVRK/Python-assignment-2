# =============================================================================
# 📌 AI API Integration Assignment - Google Gemini API
# =============================================================================
# Description:
# This program connects to Google Gemini API and generates responses
# based on user input.
#
# Features:
# - Accepts user input from terminal
# - Sends request to Gemini model
# - Displays AI-generated response
# - Handles errors properly
#
# API Key Handling:
# - NOT hardcoded
# - NOT asked from user
# - Loaded securely from environment variable
# =============================================================================


import os
from google import genai


# =============================================================================
# 🔐 LOAD API KEY FROM ENVIRONMENT
# =============================================================================

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ Error: GOOGLE_API_KEY not set in environment variables.")
    print("Set it using PowerShell before running the program.")
    exit()


# Initialize Gemini client
client = genai.Client(api_key=api_key)

# Model name (latest working free model)
MODEL_NAME = "gemini-2.0-flash"


# =============================================================================
# 🚀 FUNCTION: QUERY GEMINI
# =============================================================================

def query_gemini(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:
        return f"Error: {str(e)}"


# =============================================================================
# 🧪 MAIN PROGRAM
# =============================================================================

if __name__ == "__main__":

    print("=" * 50)
    print("     Google Gemini — AI Query Program")
    print("=" * 50)
    print(f"Model: {MODEL_NAME}\n")

    user_prompt = input("Enter your prompt: ").strip()

    if not user_prompt:
        print("No prompt entered. Exiting.")
    else:
        print("\nQuerying Google Gemini API...\n")

        result = query_gemini(user_prompt)

        print("─" * 50)
        print("Response:")
        print("─" * 50)
        print(result)
        print("─" * 50)