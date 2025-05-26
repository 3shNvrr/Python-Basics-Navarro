# Students with surnames and their scores
students = {
    "Alex Asano": 87,
    "Dylan Yra": 98,           # highest score
    "Jaden Cruz": 67,            # failing
    "Joel Bacara": 90,
    "Kierra Mallari": 90,
    "Leo Martinez": 69,          # failing
    "Maya Wilson": 88,
    "Alan Yuxon": 83,
    "Nina Panganiban": 78,
    "Raquel Garcia": 92,
    "Rain Torres": 68,           # failing
    "Sean Macato": 85,
    "Stefannie Baccay": 79,
    "Tina Santos": 85,
    "Yuri Rodriguez": 93,
}

def calculate_average(scores):
    total = sum(scores)
    count = len(scores)
    average = total / count
    return average

def find_top_students(students_dict):
    max_score = max(students_dict.values())
    top_students = [name for name, score in students_dict.items() if score == max_score]
    return top_students, max_score

def list_failing_students(students_dict, passing_score=70):
    failing = {name: score for name, score in students_dict.items() if score < passing_score}
    return failing

# Calculate average score
average_score = calculate_average(list(students.values()))
print(f"Average score of the class: {average_score:.2f}")

# Find top student(s)
top_students, top_score = find_top_students(students)
print(f"Top student(s) with score {top_score}: {', '.join(top_students)}")

# List students who are failing (score below 70), sorted alphabetically
failing_students = list_failing_students(students)
if failing_students:
    print("Students failing (score below 70):")
    for name in sorted(failing_students):
        print(f"- {name}: {failing_students[name]}")
else:
    print("No students are failing.")
