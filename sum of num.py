a=int(input())
sum=0
fact=1
for i in range(1,a+1):
    fact*=i
    sum+=fact
print(sum)   
