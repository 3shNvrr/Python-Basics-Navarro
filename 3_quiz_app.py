# Mini Quiz App: Country Capitals Quiz with specified countries

quiz_questions = {
    "What is the capital of the Philippines?": "Manila",
    "What is the capital of Canada?": "Ottawa",
    "What is the capital of Japan?": "Tokyo",
    "What is the capital of South Korea?": "Seoul",
    "What is the capital of Brunei?": "Bandar Seri Begawan",
    "What is the capital of Belgium?": "Brussels",
    "What is the capital of France?": "Paris",
    "What is the capital of Australia?": "Canberra",
    "What is the capital of Mexico?": "Mexico City",
    "What is the capital of India?": "New Delhi"
}

# Predefined answers (hardcoded)
user_answers = [
    "Manila",               # correct
    "Ottawa",               # correct
    "Tokyo",                # correct
    "Busan",                # wrong, correct is Seoul
    "Bandar Seri Begawan",  # correct
    "Brussels",             # correct
    "Paris",                # correct
    "Sydney",               # wrong, correct is Canberra
    "Mexico City",          # correct
    "New Delhi"             # correct
]

def calculate_score(questions, answers):
    score = 0
    for i, (question, correct_answer) in enumerate(questions.items()):
        if answers[i].strip().lower() == correct_answer.lower():
            score += 1
    return score

final_score = calculate_score(quiz_questions, user_answers)
print(f"You scored {final_score} out of {len(quiz_questions)}.")
