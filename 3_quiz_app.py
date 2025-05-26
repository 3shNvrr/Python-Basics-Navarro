# Mini Quiz App using dictionaries and basic logic

def run_quiz():
    # Define the quiz questions and choices in a dictionary
    quiz = [
        {
            "question": "What does the acronym VPN stand for?",
            "choices": ["A. Virtual Public Network", "B. Virtual Private Network", "C. Verified Protected Network", "D. Very Private Network"],
            "answer": "B"
        },
        {
            "question": "What type of malware demands payment to restore access to your data?",
            "choices": ["A. Virus", "B. Spyware", "C. Ransomware", "D. Worm"],
            "answer": "C"
        },
        {
            "question": "What is phishing?",
            "choices": ["A. A type of firewall", "B. An attack that tricks users into revealing personal info", "C. A security patch", "D. A password manager"],
            "answer": "B"
        },
        {
            "question": "Which of the following is a strong password?",
            "choices": ["A. password123", "B. abcdefg", "C. Qw!8$zL9", "D. 123456"],
            "answer": "C"
        },
        {
            "question": "What does a firewall do?",
            "choices": ["A. Cools down your computer", "B. Filters incoming and outgoing traffic", "C. Deletes old files", "D. Encrypts documents"],
            "answer": "B"
        },
        {
            "question": "Which of these is a common sign of a phishing email?",
            "choices": ["A. Correct grammar", "B. Official logo", "C. Urgent request for personal info", "D. Personal greeting"],
            "answer": "C"
        },
        {
            "question": "What is two-factor authentication?",
            "choices": ["A. Using two passwords", "B. A second layer of security requiring something you know and something you have", "C. Using a backup email", "D. Changing passwords regularly"],
            "answer": "B"
        },
        {
            "question": "What is the main purpose of encryption?",
            "choices": ["A. Backup files", "B. Hide files from others", "C. Protect data by making it unreadable without a key", "D. Speed up your computer"],
            "answer": "C"
        },
        {
            "question": "Which device is used to protect a network by monitoring and controlling incoming and outgoing traffic?",
            "choices": ["A. Router", "B. Switch", "C. Firewall", "D. Modem"],
            "answer": "C"
        },
        {
            "question": "What is social engineering in cybersecurity?",
            "choices": ["A. A software bug", "B. Human-based manipulation to gain access or information", "C. A hardware issue", "D. Internet protocol"],
            "answer": "B"
        }
    ]

    # Predefined user answers (simulate user input)
    user_answers = ["B", "C", "B", "C", "B", "C", "B", "C", "C", "B"]

    score = 0

    for i in range(len(quiz)):
        q = quiz[i]
        print(f"Q{i+1}: {q['question']}")
        for choice in q["choices"]:
            print(choice)

        user_answer = user_answers[i]
        print(f"Your answer: {user_answer}")

        if user_answer.upper() == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.\n")

    print(f"Your final score is {score} out of {len(quiz)}.")

# Run the quiz
run_quiz()
