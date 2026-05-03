from crewai import Agent
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["OPENAI_API_KEY"] ="open_apikey"

# ─── AGENTS ───
code_reviewer = Agent(
    role="Senior Android Code Reviewer",
    goal="Review Kotlin code for SOLID principles, clean architecture and best practices",
    backstory="""You are a Principal Android Engineer with 13+ years of experience.
    You have reviewed thousands of Kotlin files and know every best practice.""",
    llm="groq/llama-3.3-70b-versatile",  # ← string format!
    verbose=True
)

security_expert = Agent(
    role="Android Security Expert",
    goal="Find security vulnerabilities in Android Kotlin code",
    backstory="""You are an Android security specialist.
    You know JWT, SSL Pinning, BiometricPrompt, encryption — everything.""",
    llm="groq/llama-3.3-70b-versatile",
    verbose=True
)

performance_reviewer = Agent(
    role="Android Performance Expert",
    goal="Find memory leaks, ANR issues and performance problems in Kotlin code",
    backstory="""You are an Android performance expert.
    You have fixed hundreds of OOM, ANR and memory leak issues.""",
    llm="groq/llama-3.3-70b-versatile",
    verbose=True
)

report_writer = Agent(
    role="Technical Report Writer",
    goal="Write a professional code review report in table format",
    backstory="""You write clear, structured technical reports
    that developers can immediately act upon.""",
    llm="groq/llama-3.3-70b-versatile",
    verbose=True
)
