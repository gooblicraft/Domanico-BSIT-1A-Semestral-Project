#Edriane Domanico IT-Paradigm Activity 

# user dictionaries
user_credentials = {
    "user1": "password123",
    "user2": "mypassword",
    "admin": "adminpass"
}

# Function para sa user log in
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username in user_credentials and user_credentials[username] == password:
        print(f"Welcome, {username}!")
        return True
    else:
        print("Invalid username or password. Please try again.")
        return False

# Function para sa arithmetic operations
def perform_operations():
    results = []  # List to store results
    operations = {
        "1": "Addition",
        "2": "Subtraction",
        "3": "Multiplication",
        "4": "Division",
        "5": "Exit"
    }
    
    while True:
        print("\nChoose an operation:")
        for key, value in operations.items():
            print(f"{key}: {value}")
        
        choice = input("Enter your choice: ")
        
        if choice == "5":
            break
        
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            if choice == "1":
                result = num1 + num2
            elif choice == "2":
                result = num1 - num2
            elif choice == "3":
                result = num1 * num2
            elif choice == "4":
                result = num1 / num2 if num2 != 0 else "undefined (division by zero)"
            else:
                print("Invalid choice. Please try again.")
                continue
            
            print(f"Result: {result}")
            results.append(result)
        except ValueError as e:
            print(f"Error: {e}")
    
    return results

# Main function
def main():
    if login():
        results = perform_operations()
        print("\nAll results:", results)

# Run the main function
if __name__ == "__main__":
    main()
