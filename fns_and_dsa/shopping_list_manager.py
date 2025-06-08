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
            item = input("Enter the item name: ").lower().strip()
            shopping_list.append(item)
            print(shopping_list)
        elif choice == '2':
            item = input("Enter the item name: ").lower().strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"Removed the item {item}")
            else:
                print(f"Couldn't find the item {item}.")
        elif choice == '3':
            if shopping_list:
                for items in shopping_list:
                    print(items)
            else:
                print("Shopping list is empty")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()