# =============================================================================
# 📌 AI API Integration Assignment - Hugging Face
#
# Description:
# This program uses Hugging Face Inference API to generate AI responses.
# It uses a powerful open-source model via Hugging Face providers.
# =============================================================================

import os
from huggingface_hub import InferenceClient

# API CONFIGURATION
api_key = os.getenv("HUGGINGFACE_API_KEY")

if not api_key:
    raise EnvironmentError(
        "HUGGINGFACE_API_KEY is not set.\n"
        "Set it using environment variables."
    )

# Initialize client
client = InferenceClient(provider="auto", api_key=api_key)

MODEL_ID = "Qwen/Qwen2.5-72B-Instruct"


# FUNCTION
def query_huggingface(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model=MODEL_ID,
            messages=[
                {"role": "system", "content": "Helpful assistant"},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error: {str(e)}"


# MAIN
if __name__ == "__main__":
    prompt = input("Enter prompt: ")
    print(query_huggingface(prompt))