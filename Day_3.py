# while loop.
# add natural numbers upto n;
# n=int(input("Enter n:"))
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i=i+1
# print("Rhe sum :",sum)

# loop control statement

# break
# continue
# pass

# to find lcm and gcd

# n1=int(input("Enter the n1: "))
# n2=int(input("Enter the n2: "))
# m1=n1
# m2=n2
# mul=n1*n2
# while (n1!=n2):
#     if(n1>n2):
#         n1=n1-n2
#     else:
#         n2=n2-n1
# n1=n2
# print("GCD :",n1)
# print("LCM :",(m1*m2)/n1)

# print prime number in a given range
n1=int(input("Upper limit :"))
n2=int(input("Lower limit :"))
x=2
for x in range(n1,n2+1):
    while(x<n2/2):
        if(n2%x==0):
            x=x+1
