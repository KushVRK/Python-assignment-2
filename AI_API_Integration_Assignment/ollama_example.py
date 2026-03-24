# =============================================================================
# 📌 AI API Integration Assignment - Ollama (Local Model)
#
# Description:
# This program interacts with a locally running Ollama model.
# No API key required.
# =============================================================================

import requests

BASE_URL = "http://localhost:11434/api/generate"


def query_ollama(prompt: str) -> str:
    try:
        response = requests.post(
            BASE_URL,
            json={
                "model": "tinyllama",
                "prompt": prompt,
                "stream": False
            }
        )
        return response.json()["response"]

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    prompt = input("Enter prompt: ")
    print(query_ollama(prompt))# =============================================================================
# 📌 AI API Integration Assignment - Ollama (Local Model)
# =============================================================================
# Description:
# This program connects to a locally running Ollama model.
# It sends user input and receives AI-generated responses.
#
# Features:
# - Works completely offline (local model)
# - Accepts user input
# - Sends request to Ollama API
# - Displays response
# - Handles errors properly
#
# Note:
# - No API key is required
# - Ollama must be running locally
# =============================================================================


import requests


# =============================================================================
# ⚙️ OLLAMA CONFIGURATION
# =============================================================================

# Local Ollama API endpoint
BASE_URL = "http://localhost:11434/api/generate"

# Model name (make sure it's installed)
MODEL_NAME = "tinyllama"


# =============================================================================
# 🚀 FUNCTION: QUERY OLLAMA
# =============================================================================

def query_ollama(prompt: str) -> str:
    try:
        response = requests.post(
            BASE_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            }
        )

        response.raise_for_status()

        return response.json().get("response", "No response received.")

    except requests.exceptions.ConnectionError:
        return "❌ Error: Ollama is not running. Start it using 'ollama serve'."

    except Exception as e:
        return f"Error: {str(e)}"


# =============================================================================
# 🧪 MAIN PROGRAM
# =============================================================================

if __name__ == "__main__":

    print("=" * 50)
    print("        Ollama — AI Query Program")
    print("=" * 50)
    print(f"Model: {MODEL_NAME}\n")

    user_prompt = input("Enter your prompt: ").strip()

    if not user_prompt:
        print("No prompt entered. Exiting.")
    else:
        print("\nQuerying Ollama (local model)...\n")

        result = query_ollama(user_prompt)

        print("─" * 50)
        print("Response:")
        print("─" * 50)
        print(result)
        print("─" * 50)