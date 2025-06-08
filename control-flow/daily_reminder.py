
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()


match priority:
    case "high" | "medium":
        reminder = f"Reminder: '{task}' is a {priority} priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
    case "low":
        if time_bound == "yes":
            reminder = f"Reminder: '{task}' is a low priority task that requires immediate attention today!"
        else:
            reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = f"Task: '{task}'"

print("\n" + reminder)