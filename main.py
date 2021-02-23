# print out numbers 1 - 10

counter = 1
while(counter <= 10): # or (counter < 11):
  print(counter)
  counter += 1

# print out all even numbers between 1 - 20

number = 2
while(number <= 20):
  print(number)
  number += 2

# Ask the user for a number
# Print all the numbers up to user's number starting 1

counter = 1
question = int(input("Choose a number: "))
while(counter <= question):
  print(counter)
  counter += 1

# while():
#    if(condition)
#        print()

# Alternative way to print even numbers

counter = 1
while(counter <= 20):
  if(counter % 2 == 0):
    print(counter)
  counter += 1

# Print all numbers between 1 - 100 that are divisible by 3 and 7
# BUT NOT BOTH

counter = 1
while(counter <= 100):
  if(counter % 3 == 0 or counter % 7 == 0):
    if not(counter % 3 == 0 and counter % 7 == 0):
      print(counter)
  counter += 1

# Print all the numbers between 1 - 100
# If the number is divisable by 3, print out "Fizz"
# If the number is divisable by 5, print out "Buzz"
# If the number is divisable by BOTH, print out "FizzBuzz"

counter = 1
while(counter <= 100):
  if(counter % 3 == 0 and counter % 5 == 0):
    print("FizzBuzz")
  elif(counter % 3 == 0):
    print("Fizz")
  elif(counter % 5 == 0):
    print("Buzz")
  else:
    print(counter)
  counter += 1
  

