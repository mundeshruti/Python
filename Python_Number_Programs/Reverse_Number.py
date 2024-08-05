def reverse_num(n):
    m=0
    while(n!=0):
        rem=n%10
        m= (m*10)+rem
        n=n//10
    return m
n=int(input("Enter Number: "))
print("Reverse of Number is:",reverse_num(n))
