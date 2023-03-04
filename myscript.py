"""
This is a docstring.
It's a multi-line comment that describes what the script does.
It's a good idea to include a docstring at the top of your script.

Purpose
-------

This script is a collection of examples of Python code.
It's meant to be run from the command line.

How To Run
----------

To run this script, open a terminal window and type:

python myscript.py

You should see the output of the script printed to the terminal.

To run this script and save the output to a file, type:

python myscript.py > output.txt

VS Code
-------

VS Code has a built-in terminal window.

You can run this script from within VS Code.
Open the script in VS Code and press F5 to run it.

"""




# Define a string variable
message = "Hello, world!"

# Print the variable to the console
print(message)

# Print the variable to the console
# use an f-string to print some text and the value of the variable
print(f"message = {message}")

# Print the type of the variable
what_type = type(message)
print(f"message is of type {what_type}")

# Define an integer variable
age = 25

# Define a float variable
height = 1.75

# Define a boolean variable
is_student = True

# LISTS ..............................

# Define a list variable
fruits = ['apple', 'banana', 'cherry']

# Print a message and the value of each variable
print(f"age = {age}")
print(f"height = {height}")
print(f"is_student = {is_student}")
print(f"fruits = {fruits}")

# Print the first item in the list
# The first item is at index 0
# which makes sense - it's zero away from the beginning of the list! 
print(fruits[0])

# Print the second item in the list
# This is one away from the beginning of the list
# It's a bit confusing, 
# but it's a common convention - we get used to it quickly
print(fruits[1])

# Add a new item to the list
# every Python list has a method called append()
# pass in whatever you want to add to the list
# we've got an apple, banna, and cherry, so let's add an orange
fruits.append('orange')

# print the list now that we've added an item
print(f"fruits = {fruits}")

# Use a for loop to print each item in the list

print("Fruits:")

for fruit in fruits:
    print(fruit)


# DICTIONARY ..............................


# Define a dictionary variable
# A dictionary is a collection of key-value pairs
# Works great for storing data about a person
person = {'name': 'Alice', 'age': 30, 'is_student': True}

print("Person:")

# Print the value associated with the 'name' key
print(person['name'])

# Print the value associated with the 'age' key
print(person['age'])

# Print the value associated with the 'is_student' key
print(person['is_student'])


# DO DIFFERENT THINGS BASED ON CONDITIONS .............................

# Use a conditional statement to print a message

print (f"age = {age}")

if age < 18:
    print("You are too young to vote.")
elif age >= 18 and age < 65:
    print("You are eligible to vote.")
else:
    print("You are old enough to be eligible to vote by mail.")



# Define a function that takes two arguments and returns their sum
def add_two(x, y):
    return x + y

# Define a function that takes three arguments and returns their sum
# something is wrong with our logic. 
# Can you fix it?
def add_three(x, y, z):
    return x + y 


# Call a function with two arguments
# and assign the result to a variable named sum
sum = add_two(5, 7)

# Print the value of the sum variable
print(sum)

# Call the function with three arguments and print the result
result = add_three(5, 7, 9)

# Print the value of the result variable
print(result)

