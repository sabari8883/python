
numbers = [10, 15, 22, 20, 25, 18, 20, 30]

found_20 = False

for num in numbers:
    if num == 20 and not found_20:
        found_20 = True
    elif not found_20 and num % 2 == 0:
        print(num)
    if found_20:
        break
