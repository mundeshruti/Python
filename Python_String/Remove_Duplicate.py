s = input("enter string: ")
p = ""
for char in s:
    if char not in p:
        p = p+char
print(p)
k = list(s)