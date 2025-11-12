task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ") 

match priority:
    case "high":
        if time_bound == "yes":
            priority_message = f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!"
        else:
            priority_message = f"Reminder: '{task}' is a {priority} priority task. Consider completing it when you have free time."
    case "medium":
        if time_bound == "yes":
            priority_message = f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!"
        else:
            priority_message = f"Reminder: '{task}' is a {priority} priority task. Consider completing it when you have free time."
    case "low":
        if time_bound == "yes":
            priority_message = f"Reminder: '{task}' is a {priority} task that requires immediate attention today!"
        else:
            priority_message = f"Reminder: '{task}' is a {priority} task. Consider completing it when you have free time."
    case _:
        priority_message = "Error: Invalid priority level entered."

print(priority_message)