def is_happy_number(num):

    visited = set()
    def sum_of_squares(n):
        total = 0
        while n > 0:
            digit = n % 10
            total += digit ** 2
            n //= 10
        return total
    while num != 1:
        num = sum_of_squares(num)
        if num in visited:
            return False
        visited.add(num)
    
    return True
given_number = int(input("Enter number: "))

if is_happy_number(given_number):
    print("Given number is a Happy number")
else:
    print("Given number is not a Happy number")
