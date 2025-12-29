# 🔥 PromptForge

**PromptForge** is a portfolio‑grade **AI Red Teaming & Prompt Injection Testing Framework** designed to evaluate the security posture of Large Language Models (LLMs) against adversarial prompt-based attacks.

> ⚔️ *Weaponizing prompts to test AI defenses.*

---

## 📌 What is PromptForge?

PromptForge is an **offensive AI security lab** that simulates real-world **prompt injection, role confusion, and policy bypass attacks** against LLMs under different security configurations.

It is built for:
- AI Red Teaming
- LLM Security Research
- Prompt Injection Practice
- Model Defense Benchmarking
- Security Portfolios

---

## 🚀 Key Features

### Core Capabilities
- ✅ Goal-based AI exploitation challenges  
- ✅ Multiple security levels (Easy vs Hard)  
- ✅ Automatic attack success detection  
- ✅ Attempt-based scoring system  
- ✅ Attack logging & replay  
- ✅ Modular & extensible architecture  

### Advanced Capabilities
- 🔥 Prompt injection attacks  
- 🔥 Role confusion attacks  
- 🔥 Obfuscated prompt attacks  
- 🔥 Defense benchmarking  
- 🔥 Model-agnostic design (future-ready)  

---

## 🧠 Challenges Included

| Challenge ID | Name | Goal |
|------------|------|------|
| 1 | Phrase Injection | Force model to output a restricted phrase |
| 2 | Secret Extraction | Extract sensitive file contents |
| 3 | Unauthorized Transaction | Bypass financial restrictions |

Each challenge simulates **real AI security failure modes**.

---

## 🔐 Security Levels

| Level | Description |
|-----|-------------|
| Easy | Weak defenses, trusts user input |
| Hard | Injection-aware, refusal logic enabled |

This allows **defense strength comparison**.

---

## 📁 Project Structure
```
PromptForge/
│
├── core/ # Core engine & logic
│ ├── engine.py
│ ├── evaluator.py
│ ├── models.py
│ ├── prompts.py
│ └── scoring.py
│
├── attacks/ # Attack payload generators
│ ├── injection.py
│ ├── role_confusion.py
│ └── obfuscation.py
│
├── challenges/ # Challenge definitions
│ ├── challenge_1.py
│ ├── challenge_2.py
│ └── challenge_3.py
│
├── logs/ # Attack logs
│ └── attacks.json
│
├── main.py # Entry point
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository
```
git clone https://github.com/<your-username>/PromptForge.git
cd PromptForge
2️⃣ Create Virtual Environment (Recommended) :
python3 -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies :
pip install -r requirements.txt
🔑 API Configuration :
export GEMINI_API_KEY="your_api_key_here"
▶️ Usage :
python main.py
```

🧪 Attack Logging
All attacks are automatically logged to:
```
logs/attacks.json
```
Each log includes:
- Timestamp
- Challenge ID
- Prompt payload
- Model response
- Success status

🛡️ Ethical Use Notice :
PromptForge is intended strictly for defensive security testing, research, and education.

🧑‍💻 Author :
Faseeh Ul Hassan
AI Red Teaming | LLM Security | Prompt Injection Research

📌 GitHub: @faseeh-ul-hassan
📌 Focus: Agentic AI Security, Prompt Injection, Model Exploitation

📜 License :
This project is licensed under the MIT License.
See LICENSE file for details.

⭐ Why This Project Matters :

PromptForge demonstrates:

- Offensive security mindset
- Understanding of LLM failure modes
- Real AI Red Teaming workflows
- Clean engineering & modular design

