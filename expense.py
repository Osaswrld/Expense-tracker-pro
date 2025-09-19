class Expense: # Define a class named Expense

  # Define the initialization method (__init__) with three parameters:
  # name, category & amount
  def __init__(self, name, category, amount) -> None:
    # Init the 'name' attribute of the expense object
    self.name = name
    # Init the 'name' attribute of the expense object
    self.category = category
    # Init the 'name' attribute of the expense object
    self.amount = amount
 
  # Define the representation method (__repr__) to provide a str rep
  # of the Expense object
  def __repr__(self):
    # Return a str representaton of the Expense object
    return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f}>"