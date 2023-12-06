#  printing patterns
#    *       *
#   * *     * *
#  * * *   * * *
# * * * * * * * *
# n=int(input("enter the range "))
# for i in range(1 , n+1):
#     for k in range(n+1-i,1,-1):
#         print(" ",end="")
#     for j in range(0,2*i-1):
#         print("*",end = "")
#     for k in range(2*(n+1-i),1,-1):
#         print(" ",end="")
#     for j in range(0,2*i-1):
#         print("*",end = "")
    
#     print("")
    
# printing the pattern 
# A B C D E
#  B C D E
#   C D E

rows = 3
for i in range(rows):
    for j in range(i):
        print("", end=" ")
    for k in range(i-2, rows):
        print(chr(65 + k+2), end=" ")
        

    print()

