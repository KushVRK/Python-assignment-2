# multi_api_query.py
# Assignment: AI API Integration - Unified Multi-Provider Query Program (BONUS)

# Supported providers: Groq, Ollama, Hugging Face, Cohere

import os
import sys


# ── Provider: Groq ────────────────────────────────────────────────────────────
def query_groq(prompt: str) -> str:
    """Query Groq Llama-3.1-8B-Instant."""
    try:
        from groq import Groq
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            return "Error: GROQ_API_KEY is not set."
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model =  "llama-3.1-8b-instant",   # updated — llama3-8b-8192 is decommissioned
            messages=[
                {"role": "system", "content": "You are a helpful and concise AI assistant."},
                {"role": "user",   "content": prompt},
            ],
            max_tokens=500,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Groq Error: {e}"


# ── Provider: Ollama (local) ──────────────────────────────────────────────────
def query_ollama(prompt: str) -> str:
    """Query a locally running Ollama model."""
    try:
        import requests

        # Check if Ollama server is running
        try:
            tags = requests.get("http://localhost:11434/api/tags", timeout=3).json()
        except Exception:
            return (
                "Ollama Error: Server not running.\n"
                "  Fix: open a new terminal and run -> ollama serve"
            )

        # Check if any model is available
        models = [m["name"] for m in tags.get("models", [])]
        if not models:
            return (
                "Ollama Error: No models installed.\n"
                "  Fix: run -> ollama pull llama3"
            )

        # Use first available model (prefer llama3 variants)
        model = next((m for m in models if "llama3" in m.lower()), models[0])

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False,
                "options": {"temperature": 0.7, "num_predict": 500},
            },
            timeout=120,
        )
        response.raise_for_status()
        return f"[Model: {model}]\n" + response.json().get("response", "No response.").strip()

    except Exception as e:
        return f"Ollama Error: {e}"


# ── Provider: Hugging Face ────────────────────────────────────────────────────
def query_huggingface(prompt: str) -> str:
    """Query Hugging Face via Inference Providers API (Qwen2.5-72B)."""
    try:
        from huggingface_hub import InferenceClient
        api_key = os.getenv("HUGGINGFACE_API_KEY")
        if not api_key:
            return "Error: HUGGINGFACE_API_KEY is not set."
        client = InferenceClient(provider="auto", api_key=api_key)
        response = client.chat.completions.create(
            model="Qwen/Qwen2.5-72B-Instruct",
            messages=[
                {"role": "system", "content": "You are a helpful and concise AI assistant."},
                {"role": "user",   "content": prompt},
            ],
            max_tokens=500,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Hugging Face Error: {e}"


# ── Provider: Cohere ──────────────────────────────────────────────────────────
def query_cohere(prompt: str) -> str:
    """Query Cohere Command-R-Plus."""
    try:
        import cohere
        api_key = os.getenv("COHERE_API_KEY")
        if not api_key:
            return "Error: COHERE_API_KEY is not set."
        client = cohere.Client(api_key=api_key)
        response = client.chat(
            model="command-r-plus-08-2024",
            message=prompt,
            preamble="You are a helpful and concise AI assistant.",
            temperature=0.7,
            max_tokens=500,
        )
        return response.text.strip()
    except Exception as e:
        return f"Cohere Error: {e}"


# ── Provider Registry ─────────────────────────────────────────────────────────
PROVIDERS = {
    "1": ("Groq           (Llama-3.1-8B-Instant)", query_groq),
    "2": ("Ollama         (local model)",           query_ollama),
    "3": ("Hugging Face   (Qwen2.5-72B)",           query_huggingface),
    "4": ("Cohere         (Command-R-Plus)",        query_cohere),
}


# ── UI Helpers ────────────────────────────────────────────────────────────────
def print_menu():
    print("\n" + "=" * 52)
    print("        Multi-API AI Query Tool")
    print("        CampusPe — Generative AI Assignment")
    print("=" * 52)
    print("  Select an AI provider:\n")
    for key, (name, _) in PROVIDERS.items():
        print(f"    [{key}]  {name}")
    print("\n    [0]  Quit")
    print("=" * 52)


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("\nWelcome to the Multi-API Query Tool!")
    print("Ensure your API keys are set as environment variables.")

    while True:
        print_menu()
        choice = input("\nYour choice: ").strip()

        if choice == "0":
            print("\nGoodbye! 👋")
            sys.exit(0)

        if choice not in PROVIDERS:
            print("⚠  Invalid choice. Please enter a number from 0 to 4.")
            continue

        provider_name, query_fn = PROVIDERS[choice]
        print(f"\nProvider selected: {provider_name.strip()}")

        user_prompt = input("Enter your prompt: ").strip()
        if not user_prompt:
            print("No prompt entered. Returning to menu.")
            continue

        print(f"\nQuerying {provider_name.strip()}...\n")
        result = query_fn(user_prompt)

        print("─" * 52)
        print("Response:")
        print("─" * 52)
        print(result)
        print("─" * 52)

        again = input("\nQuery another provider? (y/n): ").strip().lower()
        if again != "y":
            print("\nGoodbye! 👋")
            break


if __name__ == "__main__":
    main()