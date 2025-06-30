import os

class EmployeeManager:
    def __init__(self, filename="employees.txt"):
        self.filename = filename
        self.employees = self.load_employees()

    # Loading data from file
    def load_employees(self):
        employees = []
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    for line in file:
                        parts = line.strip().split('|')
                        if len(parts) >= 4:
                            emp = {
                                "Name": parts[0],
                                "Age": int(parts[1]),
                                "Designation": parts[2],
                                "Salary": int(parts[3])
                            }
                            if len(parts) == 5:
                                emp["Previous Salary"] = int(parts[4])
                            employees.append(emp)
            except Exception as e:
                print(f"Error loading file: {e}")
        return employees

    # Saving data to file
    def save_employees(self):
        try:
            with open(self.filename, 'w') as file:
                for emp in self.employees:
                    line = f"{emp['Name']}|{emp['Age']}|{emp['Designation']}|{emp['Salary']}"
                    if "Previous Salary" in emp:
                        line += f"|{emp['Previous Salary']}"
                    file.write(line + "\n")
        except Exception as e:
            print(f"Error saving file: {e}")

    # Creating the employees
    def create(self):
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
                    continue

                emp = {
                    "Name": name,
                    "Age": age,
                    "Designation": designation.title(),
                    "Salary": salary
                }

                self.employees.append(emp)
                self.save_employees()
                print("Employee record created and saved successfully.")
            except ValueError as ve:
                print(f"Error: {ve}")

            cont = input("Thank you for using our software. Would you like to continue? (yes/no): ").strip().lower()
            if cont != 'yes':
                break

    # Displaying employees
    def display(self):
        print("\n--- Employee Records ---")
        if not self.employees:
            print("No employee records to display.\n")
            return

        for idx, emp in enumerate(self.employees, start=1):
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

    # Raising salary
    def raise_salary(self):
        print("\n--- Raise Salary ---")
        if not self.employees:
            print("No employee records found.\n")
            return

        name = input("Enter the employee name to raise salary: ")
        found = False
        for emp in self.employees:
            if emp["Name"].lower() == name.lower():
                try:
                    percent = int(input(f"Enter raise percentage for {name} (1% to 30%): "))
                    if not (1 <= percent <= 30):
                        raise ValueError("Raise percentage must be between 1 and 30.")

                    emp["Previous Salary"] = emp["Salary"]
                    hike = emp["Salary"] * percent // 100
                    emp["Salary"] += hike
                    self.save_employees()
                    print(f"Salary updated! Previous salary: ₹{emp['Previous Salary']}, New salary: ₹{emp['Salary']}\n")
                    found = True
                    break
                except ValueError as ve:
                    print(f"Error: {ve}")
                    return
        if not found:
            print(f"No employee found with the name '{name}'.\n")

    # Main menu
    def menu(self):
        while True:
            print("====== Employee Management Menu ======")
            print("1. Create Employee")
            print("2. Display Employees")
            print("3. Raise Salary")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                self.create()
            elif choice == '2':
                self.display()
            elif choice == '3':
                self.raise_salary()
            elif choice == '4':
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1 to 4.\n")

if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()
