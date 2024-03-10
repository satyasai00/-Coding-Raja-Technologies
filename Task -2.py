#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import os
from collections import defaultdict

# Constants
DATA_FILE = 'budget_data.json'

# Check and create the data file if it doesn't exist
def initialize_data_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as file:
            file.write('{}')
        print("Storage file created successfully.")
    else:
        print("Storage file already exists.")

# Default data structure for transactions
all_transactions = defaultdict(list)

# Save data to the file
def save_data():
    with open(DATA_FILE, 'w') as file:
        json.dump(all_transactions, file)

# Load data from the file
def load_data():
    global all_transactions
    try:
        with open(DATA_FILE, 'r') as file:
            all_transactions = json.load(file)
    except FileNotFoundError:
        all_transactions = defaultdict(list)

    # Ensure keys exist even if the file was created newly
    all_transactions.setdefault('income', [])
    all_transactions.setdefault('expense', [])

# Add a transaction to the data structure
def add_transaction(transaction_type, category, amount):
    all_transactions[transaction_type].append({'category': category, 'amount': amount})
    save_data()

# Get a valid amount input from the user
def get_valid_amount_input(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount < 0:
                print("Please enter a non-negative amount.")
            else:
                return amount
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Calculate the remaining budget
def calculate_remaining_budget():
    total_income = sum(transaction['amount'] for transaction in all_transactions['income'])
    total_expense = sum(transaction['amount'] for transaction in all_transactions['expense'])
    return total_income - total_expense

# Analyze expenses and display a summary
def analyze_expenses():
    expense_categories = defaultdict(int)
    for expense in all_transactions['expense']:
        expense_categories[expense['category']] += expense['amount']
    
    print("\nExpense Analysis:")
    for category, amount in expense_categories.items():
        print(f"{category}: ₹{amount}")

# Clear all data in the data structure
def clear_data():
    while True:
        confirmation = input("Are you sure you want to clear all data? (Yes/No): ").lower()
        if confirmation in ['yes', 'y']:
            global all_transactions
            all_transactions = defaultdict(list)
            save_data()
            print("\nAll data cleared successfully.")
            break
        elif confirmation in ['no', 'n']:
            print("Clear data operation canceled.")
            break
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

# Main menu and user interface
def main():
    load_data()
    
    while True:
        print("\n===== Main Menu =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Remaining Budget")
        print("4. Analyze Expenses")
        print("5. Clear Data")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            category = input("Enter income category: ")
            amount = get_valid_amount_input("Enter income amount: ")
            add_transaction('income', category, amount)
            print("\nIncome added successfully!")
        
        elif choice == '2':
            category = input("Enter expense category: ")
            amount = get_valid_amount_input("Enter expense amount: ")
            add_transaction('expense', category, amount)
            print("\nExpense added successfully!")
        
        elif choice == '3':
            remaining_budget = calculate_remaining_budget()
            print(f"\nRemaining Budget: ₹{remaining_budget}")
        
        elif choice == '4':
            analyze_expenses()
        
        elif choice == '5':
            clear_data()
        
        elif choice == '6':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    initialize_data_file()
    main()

