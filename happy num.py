num=int(input("enter a number: "))
visited=set()
while num>1 and num not in visited:
    visited.add(num)
    num=sum(int(char)**2 for char in str(num))
if(num==1):
    print("Happy number")
else:
    print("not a happy number")
