task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ") 

match priority:  # Changed from task_priority to priority
    case "high":  # Changed to lowercase
        if time_bound == "yes":
            priority_message = f"'{task}' is a high priority task that requires immediate attention today!"
        else:
            priority_message = f"'{task}' is a high priority task."
    case "medium":  # Changed to lowercase
        if time_bound == "yes":
            priority_message = f"'{task}' is a medium priority task that should be completed soon."
        else:
            priority_message = f"'{task}' is a medium priority task."
    case "low":  # Changed to lowercase
        if time_bound == "yes":
            priority_message = f"'{task}' is a low priority task but has a time constraint."
        else:
            priority_message = f"'{task}' is a low priority task. Consider completing it when you have free time."

print(priority_message)