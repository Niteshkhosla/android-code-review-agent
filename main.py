from crewai import Crew, Process
from dotenv import load_dotenv
from agents import (
    code_reviewer,
    security_expert,
    performance_reviewer,
    report_writer
)
from tasks import (
    code_review_task,
    security_task,
    performance_task,
    report_task
)

load_dotenv()

# Sample Kotlin code — review ke liye
kotlin_code = """
class UserRepository {
    companion object {
        val instance = UserRepository()
    }
    
    fun getUser(id: String): User {
        val db = DatabaseHelper()
        val user = db.query("SELECT * FROM users WHERE id = " + id)
        return user
    }
    
    fun savePassword(password: String) {
        SharedPreferences.edit().putString("password", password).apply()
    }
}
"""

# Crew banao
crew = Crew(
    agents=[
        code_reviewer,
        security_expert,
        performance_reviewer,
        report_writer
    ],
    tasks=[
        code_review_task,
        security_task,
        performance_task,
        report_task
    ],
    process=Process.sequential,  # ek ke baad ek
    verbose=True
)

# Kickoff!
print("🤖 Android Code Review Agent Starting...\n")
result = crew.kickoff(inputs={"kotlin_code":kotlin_code})

print("\n" + "="*50)
print("FINAL CODE REVIEW REPORT")
print("="*50)
print(result)
