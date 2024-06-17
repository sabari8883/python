
a = [15, 14, 25, 14, 32, 14, 31]
a.sort()
result = []
for num in a:
    if num not in result:
        result.append(num)

print("Sorted Array =", result)
