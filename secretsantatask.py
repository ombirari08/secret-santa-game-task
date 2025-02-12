import csv
import random
from typing import List, Dict


class Employee:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"Employee({self.name}, {self.email})"


class SecretSantaAssigner:
    def __init__(self, employees: List[Employee], previous_assignments: Dict[str, str]):
        self.employees = employees
        self.previous_assignments = previous_assignments

    def assign_secret_santa(self) -> Dict[Employee, Employee]:
        max_attempts = 10  # Try different shuffles before giving up
        for _ in range(max_attempts):
            remaining = set(self.employees)
            assignments = {}
            random.shuffle(self.employees)

            for employee in self.employees:
                choices = [e for e in remaining if
                           e.email != employee.email and e.email != self.previous_assignments.get(employee.email)]
                if not choices:
                    break  # Stop and retry
                secret_child = random.choice(choices)
                assignments[employee] = secret_child
                remaining.remove(secret_child)

            if len(assignments) == len(self.employees):  # Check if we succeeded
                return assignments

        raise ValueError("Valid Secret Santa assignment not possible after multiple attempts.")


class CSVHandler:
    @staticmethod
    def read_csv(filepath: str) -> List[Employee]:
        employees = []
        try:
            with open(filepath, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    employees.append(Employee(row['Employee_Name'], row['Employee_EmailID']))
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {filepath}")
        return employees

    @staticmethod
    def read_previous_assignments(filepath: str) -> Dict[str, str]:
        previous = {}
        try:
            with open(filepath, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    previous[row['Employee_EmailID']] = row['Secret_Child_EmailID']
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {filepath}")
        return previous

    @staticmethod
    def write_output(assignments: Dict[Employee, Employee], output_path: str):
        with open(output_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Employee_Name', 'Employee_EmailID', 'Secret_Child_Name', 'Secret_Child_EmailID'])
            for employee, secret_child in assignments.items():
                writer.writerow([employee.name, employee.email, secret_child.name, secret_child.email])


import unittest


class TestSecretSanta(unittest.TestCase):
    def setUp(self):
        self.employees = [
            Employee("Alice", "alice@example.com"),
            Employee("Bob", "bob@example.com"),
            Employee("Charlie", "charlie@example.com")
        ]
        self.previous_assignments = {"alice@example.com": "bob@example.com"}
        self.assigner = SecretSantaAssigner(self.employees, self.previous_assignments)

    def test_assignment_valid(self):
        assignments = self.assigner.assign_secret_santa()
        self.assertEqual(len(assignments), len(self.employees))
        for emp, child in assignments.items():
            self.assertNotEqual(emp.email, child.email)
            self.assertNotEqual(child.email, self.previous_assignments.get(emp.email, None))

    def test_no_repeated_pairs(self):
        assignments = self.assigner.assign_secret_santa()
        assigned_emails = set(emp.email for emp in assignments.values())
        self.assertEqual(len(assigned_emails), len(self.employees))


if __name__ == "__main__":
    try:
        employees = CSVHandler.read_csv("employees.csv")
        previous_assignments = CSVHandler.read_previous_assignments("previous_assignments.csv")
        assigner = SecretSantaAssigner(employees, previous_assignments)
        assignments = assigner.assign_secret_santa()
        CSVHandler.write_output(assignments, "new_assignments.csv")
        print("Secret Santa assignments successfully generated!")
    except (ValueError, FileNotFoundError) as e:
        print(f"Error: {e}")

    unittest.main()
