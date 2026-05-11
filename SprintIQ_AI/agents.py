from crewai import Agent
from langchain_ollama import OllamaLLM

# Local LLM
llm = OllamaLLM(model="llama3")

# Sprint Analysis Agent
sprint_analyst = Agent(
    role="Sprint Analyst",
    goal="Analyze sprint backlog and identify blockers",
    backstory="Expert agile sprint analyst",
    verbose=True,
    llm=llm
)

# Risk Assessment Agent
risk_assessor = Agent(
    role="Risk Assessor",
    goal="Identify sprint risks and project delays",
    backstory="Experienced project risk evaluator",
    verbose=True,
    llm=llm
)

# Reporting Agent
report_generator = Agent(
    role="Executive Reporting Specialist",
    goal="Generate concise sprint summary for management",
    backstory="Expert in executive reporting",
    verbose=True,
    llm=llm
)