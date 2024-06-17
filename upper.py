import math

# Get the upper limit from the user
upper_limit = int(input("Enter upper limit: "))

# List to store Pythagorean triplets
triplets = []

# Generate Pythagorean triplets up to the limit
for x in range(1, upper_limit + 1):
    if x % 2 == 0:  # Even
        y = (x // 2) ** 2 - 1
        z = (x // 2) ** 2 + 1
    else:  # Odd
        y = (x ** 2 - 1) // 2
        z = (x ** 2 + 1) // 2
    if x ** 2 + y ** 2 == z ** 2:
        triplets.append((x, y, z))

# Print the Pythagorean triplets
if triplets:
    print("Pythagorean triplets up to the limit:", upper_limit)
    for triplet in triplets:
        print(triplet)
else:
    print("No Pythagorean triplets found up to the limit:", upper_limit)
