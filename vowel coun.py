a="saveetha school of engineering"
vowels="aeiouAEIOU"
v_count=0
c_count=0
for c in a:
    if c.isalpha():
        if c in vowels:
            v_count+=1
        else:
            c_count+=1
print("v_count:",v_count)
print("c_count:",c_count)
