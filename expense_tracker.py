# Import necessary modules

# Import the expense class from the expense module
from expense import Expense
# Imort necessary modules
import calendar
# Import the datetime module to work with dates and times
import datetime

# Define the main function
def main():
  #print a message indicating that the expense tracker is running
  print(f"Running Expense Tracker!")

  # Get user input for the expense
  expense = get_user_expense() # Call the get_user_expense function to get expense dettails from the user

  #Define the file path for storing expenses
  expense_file_path = "file/expenses.csv"

  #Set the budget amount
  budget = 700000.00 # Set a budget amount of 700000.00

  # Write the user's expense to a file
  # call the save_user_expense function to save the user's expense details
  save_user_expense(expense, expense_file_path)

  # Read the file and summarize expenses
  summarize_expenses(expense_file_path, budget) # Call the summarize_expenses function to read the file and summarize expenses

  # Function to get user details
def get_user_expense():
  # Print a message indicating that the user expeense details are being collected
  print(f"Getting user Expense")

  # Get the expense name from the user
  expense_name = input("Enter the expense name: ") # Get the expense name from the user
  expense_amount = float(input("Enter the expense amount: ")) # Get the expense amount from the user and convert it to a float

  # Define expense categories
  expense_categories = ["Food", "Home", "Work", "Fun", "Music"] # Define a list of expense categories

  # Loop to prompt the user to select a valid category
  while True:
    print("Select a category:") # Print a message prompting the user to select a category
    for i, category_name in enumerate(expense_categories): # Loop through the expense categories and print them with their corresponding numbers
      print(f"{i + 1}, {category_name}") # Print the category number and name
      value_range = f"[1 - {len(expense_categories)}]" # Define the valid range of category numbers

      # Get user input for selecting a category
    selected_index = int(input(f"Enter the category number {value_range}: ")) - 1 # Get the category number from the user and convert it to an integer

    # Check if the selected index is valid
    if selected_index in range(len(expense_categories)):
      # Get the selected category 
      selected_category = expense_categories[selected_index]
      # Create an Expense object with the user's input
      new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount) 
      return new_expense # Return the Expense object
    else:
      print("Invalid category. Please try again!") # Print an error message if the choice is invalid

# Function to save user expense to a file
def save_user_expense(expense: Expense, expense_file_path):
  # Print a message indicating that the user's expense is being saved
  print(f"Saving user Expense: {expense} {expense_file_path}")

  # Open the expense file in append mode and write the expense details to it
  with open(expense_file_path, "a") as f: # Open the file in append mode
    # write the expense details to the file
    f.write(f"{expense.name},{expense.category},{expense.amount}\n")

# Function to summarize users expenses 
def summarize_expenses(expense_file_path, budget):
  # Print a message indicating that the expenses are being summarized
  print(f"Summarizing User Expenses")

  # Init an empty list to store user expenses
  expenses: list[Expense] = [] # Initialize an empty dictionary to hold the total expenses per category

  # Open the expense file in read mode and read the expense details from it
  with open(expense_file_path, "r") as f: # Open the file in read mode 
    lines = f.readlines()
    for line in lines:
      # Split each line to extract expense details
      expense_name, expense_category, expense_amount = line.strip().split(",") # Split the line into name, category, and amount
      # Create an Expense object to the list of expenses
      line_expense = Expense(
        name=expense_name,
        amount=float(expense_amount),
        category=expense_category
      )
      # Append the Expense object to the list of expenses
      expenses.append(line_expense)

      # Calculate total expenses by category
      amount_by_category = {}
      for expense in expenses:
        key = expense.category
        if key in amount_by_category:
          amount_by_category[key] += expense.amount
        else:
          amount_by_category[key] = expense.amount

    # Print expenses by category
    print("Expenses By Category:")
    for key, amount in amount_by_category.items():
      print(f"{key}: ${amount:.2f}") # Print the category and the total amount spent in that category

    # Calculate total spent
    total_spent =  sum([x.amount for x in expenses])
    print(f"Total Spent: ${total_spent:.2f}")

    # Get the current date
    now = datetime.datetime.now()

    # Calculate the remaining budget
    remaining_budget = budget - total_spent
    print(f"Remaining Budget: ${remaining_budget:.2f}")

    # Get the numeber of days in the current month
    days_in_month = calendar.monthrange(now.year, now.month)[1]

    # Calculate the remanining mumber of days in current month
    remaining_days = days_in_month - now.day

    # Calculate daily budget
    daily_budget = remaining_budget / remaining_days
    print(f"Daily Budget for the remaining {remaining_days} days: ${daily_budget:.2f}") # Print the daily budget in green

# Function to make text int terminal turn green
def green_text(text):
  return f"\033[92m{text}\033[0m" # Return the text wrapped in ANSI escape codes for green color

# Entry point of the program
if __name__ == "__main__":
  main() # Call the main function when thenscript is executed 

