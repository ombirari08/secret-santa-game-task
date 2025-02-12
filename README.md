# 🎅 Secret Santa Assignment System  

## 📌 Project Overview  

This project implements a **Secret Santa** assignment system that automatically pairs employees with a **secret child** while ensuring the following rules:  
- An employee cannot be assigned to themselves.  
- An employee cannot be assigned the same secret child as in the previous year.  
- Every employee is assigned exactly one secret child.  

The program reads employee details from a **CSV file**, generates assignments, and exports the results to a new CSV file.  

---

## 📂 Folder Structure  
📦 secret-santa-game-task 
- secretsantatask.py # Main script for Secret Santa assignment
- test_secretsanta.py # Unit tests for validation
- employees.csv # Employee data file
- previous_assignments.csv # Last year's assignments
- new_assignments.csv # Output file with new assignments
- README.md # Project documentation
- requirements.txt # Dependencies

## 🚀 Installation Guide  

### 1️⃣ Clone the Repository  

```bash
git clone https://github.com/yourusername/secret-santa-game-task.git
cd secret-santa-game-task
2️⃣ Set Up a Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
3️⃣ Install Dependencies
pip install -r requirements.txt

Usage Instructions
🎲 Run the Secret Santa Assignment
To generate Secret Santa assignments, use:
python secretsantatask.py

📝 Expected Input Files
**employees.csv**
Employee_Name	Employee_EmailID
Hamish Murray	hamish.murray@acme.com
Layla Graham	layla.graham@acme.com

📝 previous_assignments.csv
Employee_EmailID	Secret_Child_EmailID
hamish.murray@acme.com	layla.graham@acme.com

📄 Generated Output File
new_assignments.csv
| Employee_Name | Employee_EmailID | Secret_Child_Name | Secret

