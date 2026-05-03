# 🤖 Android Code Review AI Agent

> AI-powered Kotlin code reviewer — Built by Nitesh Khosla | 13+ Years Android Expert

## What it does
- **Agent 1** — Reviews SOLID principles & Clean Architecture
- **Agent 2** — Finds security vulnerabilities (SQL injection, encryption)
- **Agent 3** — Detects performance issues (ANR, memory leaks, coroutines)
- **Agent 4** — Generates professional code review report in table format

##  Flow
\```
Kotlin Code Input
      ↓
Agent 1: Code Review (SOLID, Clean Architecture)
      ↓
Agent 2: Security Check (JWT, SSL, Encryption)
      ↓
Agent 3: Performance Check (ANR, Memory, Coroutines)
      ↓
Agent 4: Professional Report Table
      ↓
Complete Code Review! 🎯
\```

## 🛠️ Tech Stack
| Technology | Purpose |
|---|---|
| Python | Core language |
| CrewAI | Multi-Agent orchestration |
| Groq LLM | Language model |
| python-dotenv | API key management |

## How to run

**1. Install dependencies**
\```
py -3.11 -m pip install -r requirements.txt
\```

**2. Add API key — create .env file**
\```
GROQ_API_KEY=your-groq-api-key
OPENAI_API_KEY=fake-key-not-needed
\```

**3. Run**
\```
py -3.11 main.py
\```

## 📊 Sample Output
\```
| Category | Issue | Severity | Fix |
|---|---|---|---|
| Security | SQL Injection | Critical | Use parameterized queries |
| Security | Plain text password | Critical | Use Android KeyStore |
| Performance | ANR risk | High | Use Coroutines |
| Code Review | God Object | Medium | Separate responsibilities |
\```

## 👨‍💻 Author
**Nitesh Khosla**
Principal Android Engineer | AI Agent Developer | 13+ Years
🔗 [LinkedIn](https://linkedin.com/in/nitesh-khosla-57574637)
🐙 [GitHub](https://github.com/Niteshkhosla)
