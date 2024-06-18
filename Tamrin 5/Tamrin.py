import sqlite3
import datetime
conn = sqlite3.connect ('ExpensesTracker.db')
cursor = conn.cursor ()
cursor.execute ('''
CREATE TABLE IF NOT EXISTS Expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    category TEXT,
    amount REAL,
    description TEXT
)
''')
conn.commit ()


def add_expense ():
    date = input ("Enter date (YYYY-MM-DD): ")
    category = input ("Enter category (e.g., Food, Transport): ")
    amount = float (input ("Enter amount: "))
    description = input ("Enter description: ")

    cursor.execute ("INSERT INTO Expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
                    (date, category, amount, description))
    conn.commit ()
    print ("Expense added successfully!")


def view_expenses ():
    cursor.execute ("SELECT * FROM Expenses")
    expenses = cursor.fetchall ()

    if expenses:
        print ("\nExpenses:")
        for expense in expenses:
            print (
                f"ID: {expense[0]}, Date: {expense[1]}, Category: {expense[2]}, Amount: {expense[3]}, Description: {expense[4]}")
    else:
        print ("No expenses found.")


def update_expense ():
    expense_id = int (input ("Enter the ID of the expense to update: "))
    new_date = input ("Enter new date (YYYY-MM-DD): ")
    new_category = input ("Enter new category (e.g., Food, Transport): ")
    new_amount = float (input ("Enter new amount: "))
    new_description = input ("Enter new description: ")

    cursor.execute ("UPDATE Expenses SET date = ?, category = ?, amount = ?, description = ? WHERE id = ?",
                    (new_date, new_category, new_amount, new_description, expense_id))
    conn.commit ()
    print ("Expense updated successfully!")


def delete_expense ():
    expense_id = int (input ("Enter the ID of the expense to delete: "))

    cursor.execute ("DELETE FROM Expenses WHERE id = ?", (expense_id,))
    conn.commit ()
    print ("Expense deleted successfully!")


def main ():
    while True:
        print ("\nPersonal Expense Tracker")
        print ("1. Add Expense")
        print ("2. View Expenses")
        print ("3. Update Expense")
        print ("4. Delete Expense")
        print ("5. Exit")

        choice = input ("Enter your choice: ")

        if choice == '1':
            add_expense ()
        elif choice == '2':
            view_expenses ()
        elif choice == '3':
            update_expense ()
        elif choice == '4':
            delete_expense ()
        elif choice == '5':
            print ("Exiting...")
            break
        else:
            print ("Invalid choice. Please try again.")

if __name__ == "__main__":
    main ()
conn.close ()
