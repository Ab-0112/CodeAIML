from crewai import Task

def create_tasks(data_text, agents):

    analysis_task = Task(
        description=f"""
        Analyze the sprint backlog data:

        {data_text}

        Identify:
        - delayed tasks
        - blockers
        - high-priority risks
        - incomplete work items
        """,
        agent=agents["analyst"]
    )

    risk_task = Task(
        description="""
        Evaluate sprint risk level.
        Suggest mitigation recommendations.
        """,
        agent=agents["risk"]
    )

    report_task = Task(
        description="""
        Generate a professional sprint summary report
        for project stakeholders.
        """,
        agent=agents["report"]
    )

    return [analysis_task, risk_task, report_task]