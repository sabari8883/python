lower_range = int(input("Enter the lower range: "))
upper_range = int(input("Enter the upper range: "))
if lower_range > upper_range:
    print("Invalid input: Lower range is greater than upper range.")
else:
    for num in range(lower_range, upper_range + 1):
        result = (num, num**2)
        print(result)
