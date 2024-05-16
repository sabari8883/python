# Take input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(f"Original values: num1 = {num1}, num2 = {num2}")
temp = num1 
num1 = num2 
num2 = temp  
print(f"Swapped values: num1 = {num1}, num2 = {num2}")
