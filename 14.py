def is_harshad_number(num):

    num_str = str(num)

    digit_sum = sum(int(digit) for digit in num_str)
    
    if num % digit_sum == 0:
        return True
    else:
        return False
given_number = int(input("Enter number: "))

if is_harshad_number(given_number):
    print("Given number is a Harshad number")
else:
    print("Given number is not a Harshad number")
