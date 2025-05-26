tasks = []

def add_task(task):
    tasks.append({'task': task, 'done': False})

def list_tasks():
    for i, t in enumerate(tasks):
        status = "[x]" if t['done'] else "[ ]"
        print(f"{i + 1}. {status} {t['task']}")

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

print("Daily Routine Tasks:")
list_tasks()
