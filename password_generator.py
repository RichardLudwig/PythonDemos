#!/usr/bin/python3

# # In this program, you can generate a strong password for your online accounts. Passwords can be generated for any length, and include letters, digits, and symbols. Just copy and paste the password to your password manager or similar application! Have fun!

# Imports
import string 
import random
import sys

# Initialize passwordLen's value to 0
passwordLen = 0 

# While passwordLen's value is less than or equal to zero
while (passwordLen <= 0): 
  # User prompt to ensure user enters a positive number as a password
  passwordLen = int(input("Enter desired password length: ")) 

# Syntax to clarify program's output
sys.stdout.write("Your new password: ")

# Iterate through the range of passwordLen's desired length
for i in range(passwordLen): 
  # Generate random integer between 1 and 3 for our choices
  num = random.randint(1, 3) 

  # If num is assigned the value of 1
  if (num == 1): 
    # Generates a random ascii letter and assigns its value to randLetter
    randLetter = random.choice(string.ascii_letters) 
    # Outputs randLetter on the same line
    sys.stdout.write(randLetter) 
  
  # If num is assigned the value of 2
  elif (num == 2): 
    # Generates a random digit and assigns its value to randDigit
    randDigit = random.choice(string.digits) 
    # Outputs randDigit on the same line
    sys.stdout.write(randDigit) 
  
  # Default option
  else:
    # Generates a random punctuation symbol and assigns its value to randSymbol
    randSymbol = random.choice(string.punctuation) 
    # Outputs randSymbol on the same line
    sys.stdout.write(randSymbol) 

# Print newline for program output clarity
print("\n")