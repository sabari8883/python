user_input = input("Enter numbers separated by spaces: ")
input_list = user_input.split()
l = [int(num) for num in input_list]
l1=[]
for i in range(len(l)):
    c=0
    for j in range(len(l)):
        if l[i]>l[j]:
            c+=1
    l1.append(c)
print(l1)
