array = [26, 28, 47, 26, 43, 51, 29,17]
non_composite_numbers = []
for num in array:
    if num < 2:
        continue
    count = 0
    for i in range(2, num):
        if num % i == 0:
            count += 1
            break
    if count == 0:
        non_composite_numbers.append(num)
print("Non-composite numbers in Array elements =", non_composite_numbers)
