import random

# Daily motivational quotes
quotes = [
    "Believe you can and you're halfway there.",
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Stay positive, work hard, make it happen."
]

# Task list
tasks = []

def add_task(task):
    tasks.append({'task': task, 'done': False})

def list_tasks():
    all_done = True
    for i, t in enumerate(tasks):
        status = "[x]" if t['done'] else "[ ]"
        message = " - Amazing!" if t['done'] else ""
        print(f"{i + 1}. {status} {t['task']}{message}")
        if not t['done']:
            all_done = False
    if all_done:
        print("\n🎉 Congratulations! You completed all your tasks. Keep up the great work! 🎉")

add_task("School classes/lectures - 8:00 AM to 12:00 PM")
add_task("Lunch break - 12:00 PM")
add_task("Practice coding  - 1:00 PM")
add_task("Study network security concepts - 3:00 PM")
add_task("Gym - 5:00 PM")
add_task("Rest - 6:00 PM")
add_task("Review notes - 7:00 PM")
add_task("Do assignment - 8:00 PM")
add_task("Me time - 9:00 PM")
add_task("Dinner and Shower time - 10:00 PM")
add_task("Sleep - 11:00 PM")

# Marking all tasks as done for demonstration
for task in tasks:
    task['done'] = True

print("Daily Routine Tasks:")
list_tasks()
print(f"\n🌟 Quote of the Day: \"{random.choice(quotes)}\" 🌟")
