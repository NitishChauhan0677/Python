import json
import os

filename = "employees.json"

# Load data from file if it exists
def load_employees():
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

# Save data to file
def save_employees(employees):
    with open(filename, 'w') as file:
        json.dump(employees, file, indent=4)

employees = load_employees()

def create():
    while True:
        print("\n--- Create Employee Record ---")
        try:
            designation = input("Enter designation (Programmer / Manager / Tester): ").strip().lower()
            name = input("Enter employee name: ")
            age = int(input("Enter age (18-60): "))

            if not (18 <= age <= 60):
                raise ValueError("Age must be between 18 and 60.")

            if designation == "programmer":
                salary = 25000
            elif designation == "manager":
                salary = 30000
            elif designation == "tester":
                salary = 20000
            else:
                print("Invalid designation! Record not created.\n")
                continue  # Skip to next

            emp = {
                "Name": name,
                "Age": age,
                "Designation": designation.title(),
                "Salary": salary
            }

            employees.append(emp)
            save_employees(employees)
            print("Employee record created and saved successfully.")
        except ValueError as ve:
            print(f"Error: {ve}")

        cont = input("Would you like to create another employee? (yes/no): ").strip().lower()
        if cont != 'yes':
            break  # Exit create loop and return to main menu

def display():
    print("\n--- Employee Records ---")
    loaded_employees = load_employees()

    if not loaded_employees:
        print("No employee records to display.\n")
        return

    for idx, emp in enumerate(loaded_employees, start=1):
        print(f"\nEmployee {idx}:")
        for key, value in emp.items():
            print(f"{key}: {value}")
    print()

def raise_salary():
    print("\n--- Raise Salary ---")
    if not employees:
        print("No employee records found.\n")
        return

    name = input("Enter the employee name to raise salary: ")
    found = False
    for emp in employees:
        if emp["Name"].lower() == name.lower():
            try:
                percent = int(input(f"Enter raise percentage for {name} (1% to 30%): "))
                if not (1 <= percent <= 30):
                    raise ValueError("Raise percentage must be between 1 and 30.")
                
                hike = emp["Salary"] * percent // 100
                emp["Salary"] += hike
                save_employees(employees)
                print(f"Salary updated! New salary of {name} is ₹{emp['Salary']}\n")
                found = True
                break
            except ValueError as ve:
                print(f"Error: {ve}")
                return
    if not found:
        print(f"No employee found with the name '{name}'.\n")

def main():
    while True:
        print("====== Employee Management Menu ======")
        print("1. Create Employee")
        print("2. Display Employees")
        print("3. Raise Salary")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            create()
        elif choice == '2':
            display()
        elif choice == '3':
            raise_salary()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 to 4.\n")

# Run the program
main()
