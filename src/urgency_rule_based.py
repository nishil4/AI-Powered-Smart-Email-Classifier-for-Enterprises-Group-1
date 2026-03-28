def detect_urgency_rule(text):

    text = text.lower()

    high_keywords = ["urgent","asap","immediately","critical","system down","emergency","deadline"]
    medium_keywords = ["soon","priority","update","review","request","schedule","meeting","approval"]

    score = 0

    for word in high_keywords:
        if word in text:
            score += 2

    for word in medium_keywords:
        if word in text:
            score += 1

    if score >= 2:
        return "High"

    elif score == 1:
        return "Medium"

    else:
        return "Low"