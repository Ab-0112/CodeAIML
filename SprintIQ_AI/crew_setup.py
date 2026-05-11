from crewai import Crew

from agents import (
    sprint_analyst,
    risk_assessor,
    report_generator
)

from tasks import create_tasks

def run_crew(data_text):

    agents = {
        "analyst": sprint_analyst,
        "risk": risk_assessor,
        "report": report_generator
    }

    tasks = create_tasks(data_text, agents)

    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        verbose=True
    )

    result = crew.kickoff()

    return result