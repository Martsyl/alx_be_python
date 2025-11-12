task = str(input("Enter the task you want to be reminded of daily: "))
task_priority = str(input("Enter the priority level (High, Medium, Low): "))
time_bound = str(input("Is the task time bound (yes, no): "))  

match task_priority:
    case "High":
        if time_bound == "yes":
            priority_message = f"{task} is a high priority task that requires immediate attention today!"
        else:
            priority_message = f"'{task}' is a high priority task."
    case "Medium":
        if time_bound == "yes":
            priority_message = f"'{task}' is a medium priority task that should be completed soon."
        else:
            priority_message = f"'{task}' is a medium priority task."
    case "Low":
        if time_bound == "yes":
            priority_message = f"'{task}' is a low priority task but has a time constraint."
        else:
            priority_message = f"'{task}' is a low priority task. Consider completing it when you have free time."


print(priority_message)