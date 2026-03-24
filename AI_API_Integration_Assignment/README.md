# 🚀 AI API Integration – Generative AI Assignment

## 📌 Project Description
This project demonstrates the integration of multiple Generative AI APIs using Python. Each program accepts user input, sends it to an AI API, and displays the generated response.

The objective of this assignment is to understand API integration, error handling, and working with real-world AI services securely using environment variables.

---

## 🤖 APIs Integrated
- OpenAI  
- Groq (LLaMA models)  
- Ollama (Local AI Model)  
- Hugging Face  
- Google Gemini  
- Cohere  

✅ Bonus: Multi-API Query Tool

---

## ⚙️ Setup Instructions

### 1. Clone Repository
```bash
git clone <your-repo-link>
cd AI-API-Integration-Assignment
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
```

### 3. Activate Virtual Environment (Windows)
```bash
.venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🔑 How to Obtain API Keys

### OpenAI
https://platform.openai.com/  
Go to API Keys → Create new key  

### Groq
https://console.groq.com/  
Generate API key  

### Hugging Face
https://huggingface.co/settings/tokens  
Create access token  

### Google Gemini
https://ai.google.dev/  
Generate API key  

### Cohere
https://dashboard.cohere.com/api-keys  
Create trial key  

### Ollama (Local)
https://ollama.com/  
Run:
```bash
ollama pull tinyllama
ollama serve
```

---

## 🔐 Environment Variables Setup (Windows PowerShell)
```bash
$env:OPENAI_API_KEY="your_key"
$env:GROQ_API_KEY="your_key"
$env:HUGGINGFACE_API_KEY="your_key"
$env:GOOGLE_API_KEY="your_key"
$env:COHERE_API_KEY="your_key"
```

---

## ▶️ How to Run Programs

### Individual APIs
```bash
python openai_example.py
python groq_example.py
python ollama_example.py
python huggingface_example.py
python gemini_example.py
python cohere_example.py
```

### Multi-API Tool (Bonus)
```bash
python multi_api_query.py
```

---

## 📸 Screenshots of Output
Screenshots are included in the `screenshots/` folder:

- openai_output.png  
- groq_output.png  
- ollama_output.png  
- huggingface_output.png  
- gemini_output.png  
- cohere_output.png  
- multi_api_output.png  

---

## ⚠️ Notes / Error Handling
Some APIs may return:
- 429 (Quota Exceeded)  
- Model not available  
- Memory issues (Ollama)  

These are expected in free-tier usage and are handled in the program.

---

## ✨ Features
- Accepts user input  
- Sends API requests  
- Displays responses  
- Handles errors properly  
- Uses environment variables for security  
- Supports multiple AI providers  
- Includes bonus multi-API tool  

---

## 📊 Conclusion
This project successfully demonstrates how to integrate multiple Generative AI APIs using Python and highlights real-world usage of AI services.

---

## 👨‍💻 Author
KUSHAL V R
kushalvr48@gmail.com
CampusPe – Generative AI Assignment