#exception handling along with file handeling age is 18-60 add percentage in salary and maximum % is 30% minimum is 1 % use 1 , 2, 3, ......30 for percentage
employees = []

def create():
    print("\n--- Create Employee Record ---")
    designation = input("Enter designation (Programmer / Manager / Tester): ").strip().lower()
    name = input("Enter employee name: ")
    age = int(input("Enter age: "))

    if designation == "programmer":
        salary = 25000
    elif designation == "manager":
        salary = 30000
    elif designation == "tester":
        salary = 20000
    else:
        print("Invalid designation! Record not created.\n")
        return

    emp = {
        "Name": name,
        "Age": age,
        "Designation": designation.title(),
        "Salary": salary
    }
    employees.append(emp)
    print("Employee record created successfully.")
    print("\nThank you for using our system.")
    
def display():
    print("\n--- Employee Records ---")
    if not employees:
        print("No employee records to display.\n")
        return

    for idx, emp in enumerate(employees, start=1):
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
            amount = int(input(f"Enter amount to raise for {name}: ₹"))
            emp["Salary"] += amount
            print(f"Salary updated! New salary of {name} is ₹{emp['Salary']}\n")
            found = True
            break
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
            cont = input("Would you like to continue? (yes/no): ").strip().lower()
            if cont != 'yes':
                print("Exiting program. Goodbye!")
                break
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
