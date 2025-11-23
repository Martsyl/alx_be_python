def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f'Item "{item}" added to the shopping list.')

        elif choice == '2':
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f'Item "{item}" removed from the shopping list.')
            else:
                print(f'Item "{item}" not found in the shopping list.')

        elif choice == '3':
            if not shopping_list:
                print("The shopping list is empty.")
            else:
                print("Shopping List:")
                for i in shopping_list:
                    print(f"- {i}")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
