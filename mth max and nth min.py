a=[14, 16, 87, 36, 25, 89, 34]
a.sort()
n=a[-1]
print("1st max num:",n)
a.sort(reverse=True)
m=a[-3]
print("3rd min num:",m)
sum=n+m
print("sum",sum)
diff=n-m
print("difference:",diff)
pro=n*m
print("product:",pro)
