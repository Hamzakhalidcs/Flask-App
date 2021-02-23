# List Comprhension

list  = ["apple", "banana", "cherry"]
new_list = []

for  x in list:
    if "a" in x:
        new_list.append(x)

a =[x for x in list if "a" in x]

b = [x for x in list if x != "apple"]
c = [x for x in list]  # making the same new_list as list
d = [x for x in range(10)]
less_5 = [x for x in range(10) if x<=5]  #printing number less than or equal to 5
upper_case = [x.upper() for x in list]
hello  = ['hello' for x in list]  #printing hello for all list element instead of existing one
banana = [x if x!="banana" else "orange" for x in list]  #printing orange instead of banana

print(banana)
print(hello)
print(upper_case)
print(new_list)
print(c)
print(less_5)