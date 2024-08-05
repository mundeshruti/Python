s1=input("enter first string: ")
s2=input("enter second string: ")
if len(s1)!=len(s2):
    print("strings are not equal")
else:
    s1=sorted(s1)
    s2=sorted(s2)
    if s1==s2:
        print("strings are Anagram")
    else:
        print("strings are not equal")