age_required = ("Hi! Welcome to the theater, as per theater rules, may I know your age? \n Type quit if you are finished. ")

while True:
  age = input(age_required)
  if age == "quit":
      break
  age = int(age)
  if age < 3:
      print(" As per the theater rules, the ticket is free in this level of age. ")
  elif age < 13: 
      print(" As per the theater rules, the ticket costs $10 in this level of age. ") 
  else: 
      print(" As per the theater rules, the ticket costs $15 in this level of age. ")