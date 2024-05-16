def is_perfect_number(num):
    if num <= 0:
        return False

    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i

    if divisors_sum == num:
        return True
    else:
        return False
given_number = int(input("Given Number: "))
if is_perfect_number(given_number):
    print("It's a Perfect Number")
else:
    print("It's not a Perfect Number")
