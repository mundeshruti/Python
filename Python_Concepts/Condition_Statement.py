n= int(input("Enter Number: "))
if(n>18):
    print("eligible to vote")
elif(n==18):
    a=input("enter a name:")
    if(a=="shrutika"):
        print("not decide yet")
    else:
        print("Ask to parents")
else:
    print("not eligible")