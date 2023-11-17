pizza = ("Hi! Welcome to the pizzeria, what toppings would you like to add to your pizza? \n Type quit if you are finished. ")

while True:
  topping = input(pizza)
  if topping != "quit":
      print(f"Okay! I'll add " + (topping) + " to your pizza.")  
  else: 
      print("Okay, Pizza now making.")
      break