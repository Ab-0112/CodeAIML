
def simple_chatbot(user_query):
    responses = {
        "What is the total revenue?": "The total revenue for each company in FY 2023 is:\n- Microsoft: $211.915 billion\n- Tesla: $96.773 billion\n- Apple: $383.3 billion",
        "How has net income changed over the last year?": "Here's the net income change from FY 2022 to FY 2023:\n- Microsoft: Decreased from $72.738B to $72.361B (−0.52%)\n- Tesla: Increased from $12.556B to $14.997B (+19.45%)\n- Apple: Decreased from $99.803B to $96.995B (−2.81%)",
        "What is the cash flow from operating activities?": "Cash Flow from Operating Activities for FY 2023:\n- Microsoft: $87.635 billion\n- Tesla: $14.923 billion\n- Apple: $118.254 billion",
        "Which company had the highest total assets in 2023?": "In FY 2023, Microsoft had the highest total assets at $411.55 billion.",
        "What is the total liabilities for each company in 2023?": "- Microsoft: $198.25 billion\n- Tesla: $48.39 billion\n- Apple: $290.437 billion"
    }
    return responses.get(user_query, "Sorry, I can only provide information on predefined queries.")
