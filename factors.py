given_number = int(input("Enter the given number: "))
N = int(input("Enter the value of N: "))
factors = [i for i in range(1, given_number + 1)if given_number % i == 0]
print(f"Number of factors = {len(factors)}")
print(f"1st {N} factors are: {', '.join(map(str, factors[:N]))}")
