# prime number defination:
# A prime number is a natural number greater than 1 that has no
#  positive divisors other than 1 and itself.
n=int(input("enter num: "))
m=n//2
flag=True
for i in range(2,m+1):
    if n%i==0:
        flag=False
        break
if flag==True:
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")