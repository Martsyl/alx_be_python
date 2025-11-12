first_number: int = int(input("Enter the first number: "))
second_number: int = int(input("Enter the second number: "))
operation: str = input("Choose the operation (+, -, *, /):")

match operation:
    case "+":
        result: int = first_number + second_number
    case "-":
        result: int = first_number - second_number  
    case "*":
        result: int = first_number * second_number
    case "/":
        if second_number != 0:
            result: float = first_number / second_number        
        else:
            result: str = "Cannot divide by zero."
    case _:
        result: str = "Error: Invalid operation selected."

# Add this print statement to display the result
print(f"The result is {result}")