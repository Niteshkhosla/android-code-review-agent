from crewai import Task
from agents import (
    code_reviewer,
    security_expert,
    performance_reviewer,
    report_writer
)

# Task 1 - Code Review
code_review_task = Task(
    description="""Review this Kotlin Android code:
    {kotlin_code}
    
    Check for:
    - SOLID principles
    - Clean Architecture
    - Kotlin best practices
    - Code smells
    - Naming conventions""",
    expected_output="Detailed code review with issues and suggestions",
    agent=code_reviewer
)

# Task 2 - Security Check
security_task = Task(
    description="""Check this Kotlin Android code for security issues:
    {kotlin_code}
    
    Check for:
    - JWT implementation
    - SSL Pinning
    - Data encryption
    - Sensitive data exposure
    - Authentication issues""",
    expected_output="Security vulnerabilities report with fixes",
    agent=security_expert
)

# Task 3 - Performance Check
performance_task = Task(
    description="""Check this Kotlin Android code for performance issues:
    {kotlin_code}
    
    Check for:
    - Memory leaks
    - ANR risks
    - Heavy main thread operations
    - Bitmap handling
    - Coroutine usage""",
    expected_output="Performance issues report with Kotlin fixes",
    agent=performance_reviewer
)

# Task 4 - Report
report_task = Task(
    description="""Create a professional code review report in table format.
    Include all findings from:
    - Code Review
    - Security Check
    - Performance Check
    
    Format as a structured table with:
    Category | Issue | Severity | Fix""",
    expected_output="Professional code review report in table format",
    agent=report_writer
)
