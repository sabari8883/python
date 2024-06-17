# Input the number
num = int(input("Enter a number: "))
visited = set()

# Loop to determine if the number is happy
while num != 1 and num not in visited:
    visited.add(num)
    num = sum(int(char) ** 2 for char in str(num))

# Output the result
if num == 1:
    print("The number is a happy number.")
else:
    print("The number is not a happy number.")
