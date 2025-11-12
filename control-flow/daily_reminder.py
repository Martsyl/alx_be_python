# daily_reminder.py

# This program reminds the user about a single, priority task for the day

while True:
    # Step 1: Prompt for a single task
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").lower().strip()
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

    print()  # For readability

    # Step 2: Process the task based on priority using match case
    match priority:
        case "high":
            message = f"'{task}' is a high priority task"
        case "medium":
            message = f"'{task}' is a medium priority task"
        case "low":
            message = f"'{task}' is a low priority task"
        case _:
            message = f"'{task}' has an unknown priority level"

    # Step 3: Adjust message if the task is time-sensitive
    if time_bound == "yes":
        message += " that requires immediate attention today!"
    else:
        message += ". Consider completing it when you have free time."

    # Step 4: Display the customized reminder
    print("Reminder:", message)
