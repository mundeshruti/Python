def getsum(n):
    sum=0
    while(n!=0):
        d=n%10
        sum=sum+d
        n = n // 10  # Use integer division to discard the fractional part
    return sum
n=int(input("Enter Number: "))
print(getsum(n))