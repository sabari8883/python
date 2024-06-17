# Sample input strings
S1 = "What"
S2 = "watch"
count = 0
for i in range(min(len(S1), len(S2))):
    if S1[i].lower() == S2[i].lower():
        count += 1
        print(i)
print("Total number of matches:")
print(count)
