import json
import os

filename = "employees.json"

# code for Loading data from file if it exists
def load_employees():
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error in loading employee data: {e}")
            return[]

    return []

# code for Saving the  data to file
def save_employees(employees):
    try:
        with open(filename, 'w') as file:
            json.dump(employees, file, indent=4)
    except IOError as e:
        print(f"Error in saving employee data:{e}")

employees = load_employees()

def create():
    while True:
        print("\n--- Employee Record ---")
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
                continue 

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

        cont = input("Thankyou for using our software.Would you like to continue? (yes/no): ").strip().lower()
        if cont != 'yes':
            break  

def display():
    print("\n--- Employee Records ---")
    loaded_employees = load_employees()

    if not loaded_employees:
        print("No employee records to display.\n")
        return

    for idx, emp in enumerate(loaded_employees, start=1):
        print(f"\nEmployee {idx}:")
        print(f"Name: {emp['Name']}")
        print(f"Age: {emp['Age']}")
        print(f"Designation: {emp['Designation']}")
        if "Previous Salary" in emp:
            print(f"Previous Salary: ₹{emp['Previous Salary']}")
            print(f"Current Salary: ₹{emp['Salary']}")
        else:
            print(f"Salary: ₹{emp['Salary']}")
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
                
                emp["Previous Salary"] = emp["Salary"] 
                hike = emp["Salary"] * percent // 100
                emp["Salary"] += hike
                save_employees(employees)
                print(f"Salary updated! Previous salary: ₹{emp['Previous Salary']}, New salary: ₹{emp['Salary']}\n")
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

main()
