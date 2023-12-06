# error and debugs

# syntax error 
# Exeption error 
# Logical error

# control statements

# if...else statement
# num=3
# if num>0:
#     print(num,"is the positive number ")
# else:
#     print("Hello")    

# # wap even and odd
# number=int(input("enter the number"))
# if(number%2==0):
#     print(number,"is even number")
# else:
#      print(number,"is odd number")
     
# else if ledder
# syntex elif

# percentage=int(input("Enter the percentage"))
# if(percentage >90):
#     print("A Grade")
# elif(90<percentage>70):
#     print("B Grade")
# elif(70<percentage>50):
#     print("C Grade ")
# else:
#     print("D grade")
    
# loops for loop
# number = range(1,100)
# for x in number:
#   print(x)

# sum=0
# for i in range(1,10):
#     sum=sum-1
#     print(sum)
# print("sum is ",sum)

# range formula 
# range(start ,stop ,stepsize)
# print(range)


# fibbonachi
# n1=0
# n2=1
# print(n1)
# print(n2)
# for x in range(1,10):
#     n3=n1+n2
#     print(n3)
#     n1=n2
#     n2=n3

# pattern   

# num=int(input("Enter the rows"))
# for x in range(0,num):
#     y=0
#     for y in range(y,x):
#         print("*", end="")
#     print("")

# reverse pattern 
# num=int(input("Enter the rows"))
# for x in range(0,num):
#     y=num
#     for y in range(x,y):
#         print("*", end="")
#     print("")


# # pyramid
# rows = int(input("Enter number of rows: "))
# k = 0
# for i in range(1,rows+1):
#     for space in range(1,(rows-i)+1):
#         print(end=" ")
#     while k!=(2*i-1):
#         print("*",end="")
#         k=k+1
#     k=0
#     print()
# print a hollow rectangle or dimonde shape.

# x = int(input("enter the number of rows you want : ")) 
# for i in range(x):
#     for j in range(x - i - 1): 
#         print(" ", end="") 
#     for j in range(2 * i + 1): 
#             if j == 0 or j == 2 * i: 
#                 print("*", end="") 
#             else: print(" ", end="") 
#     print() 
# for i in range(x - 2, -1, -1): 
#     for j in range(x - i - 1): 
#         print(" ", end="") 
#     for j in range(2 * i + 1): 
#             if j == 0 or j == 2 * i: 
#                 print("*", end="") 
#             else: print(" ", end="") 
#     print()
    
# hollo star 
for i in range(9):
    for j in range(13):
        if i==2 or i==6 or i+j==6 or j-i==6 or i-j==2 or i+j==14:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    
        