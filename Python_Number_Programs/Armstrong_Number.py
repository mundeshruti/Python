n=int(input("Enter a number: "))
sum=0
temp=n
while(n>0):
    d= n%10
    sum+=d**3
    n=n//10
if(sum==temp):
    print("Armstrong Number")
else:
    print("NOT Armstrong Number")



        
