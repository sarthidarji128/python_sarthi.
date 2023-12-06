# # diff methods of list
# # create a list 
# l=[4,9,6,1,7]
# print(l)
# print()

# # using appeng
# l.append(8)
# print(l)
# print()

# # using extend
# l.extend([23])
# print(l)
# print()

# # using l.pop(i)
# # remove item "i" from the list 

# l.pop(4)
# print(l)
# print()

# # using l.reveerse()
# # reverse the order of the item list
# l.reverse()
# print(l)
# print()

# # l.insert(i,item)
# # insert "item" at position i.
# l.insert(1,12)
# print(l)
# print()

# # l.remove(item)
# # find "item " in list and deletes it from the list

# l.remove(4)
# print(l)
# print()

# # l.sort()
# # sort the list in - place 

# l.sort(reverse=True)
# print(l)
# print()

# # multidimensional list

# l2=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# print(l2[2][1]) 

# l4=["kesa ho"]
# l3=[[13.44,2,3,4,['sarthi',l4,6,7,8]],[9,10,11,12],[13,14,15,16]]
# print(l3[0][4])
# print(len(l3[0][4][0]))


# smallest and largest number in the list
# len=int(input("Enter the number of element"))
# list=[]
# for i in range(len):
#     s=int(input("enter numbers :"))
#     list.append(s)
# print(list)

# write a program list of coutry that are member is BRCIS.check wheather the country is list or not.
# brics=['China','Russia','Brazil','South Africa','India']
# inp=str(input("Enter the country name :"))
# if inp in brics :
#     print(inp," are member of brics")
# else:
#     print(inp," are not a part brics")
    
    
# Write a program to print index at which perticular value exist , if the value exist at multiple location in the list than the print all the indices. also count the number of time is value isi repeated is

# list=[1,2,3,4,5,6,7,8,9,0,1,22,33,44,55,66,7,66,77,98]
# print(list)
# s=int(input("Enter the value in the list: "))
# print('Index number are : ',list.index(s))


# lakshy bhai code.
# n=int(input("Enter number of elements: "))
# list=[]
# count=0
# for i in range(n):
#     a=int(input("Enter element: "))
#     list.append(a)
# print(list)
# b=int(input("Enter element to search for: "))
# for i in range(n):
#     if list[i]==b:
#         count+=1
#         print("Index:",i)
# print("\nCount:",count)


# Ma'am method 
# list=[1,2,3,4,5,6,7,8,9,0,1,22,33,44,55,66,7,66,77,98]
# n=int(input("Enter the value to be serched"))
# i=0
# count=0
# while i<len(list):
#     if n == list[i]:
#         print(n,"Found at location",i)
#         count+=1
#     i+=1
# print(n,"appears",count,"times in the list")



# wap form list of first character of every word in another list
# Lakshybhai code
# n=int(input("Enter number of elements: "))
# list=[]
# list1=[]
# for i in range(n):
#     a=input("Enter word: ")
#     list.append(a)
# print(list)
# for i in range(n):
#     list1.append(list[i][0])
# print(list1)

# my code
# list=['sarthi','chaitu','jeevan','sparsh','karunesh']
# list2=[]
# for word in list:
#     list2.append(word[0])
# print(list2)


# # wap to add two matrices 
# x=[[2,5,4],[1,3,9],[7,6,2]]
# y=[[1,8,5],[7,3,6],[4,0,9]]
# sum=[[0,0,0],[0,0,0],[0,0,0]]
# sum1=[[0],[0],[0]]
# n=0
# for i in range(len(x)):
#     for j in range(len(y)):
#         sum[i][j]=x[i][j]+y[i][j]
# print(sum)
# for i in range(len(x)):
#     n=sum[x[0][1]]+sum[i]+sum[i]
#     sum1=n
# print(sum1)

# write a program circulate the value of n variabes 
# n=int(input("Enter number of elements: "))
# list=[]
# for i in range(n):
#     a=int(input("Enter element: "))
#     list.append(a)
# print(list)
# for i in range(n):
#     c=list.pop(0)
#     list.append(c)
#     print(list)



# tuple
# myTuple=(1,0)
# print(myTuple[1])

# tuple with if 
# myTuple=(1,0)
# if 1 in myTuple:
#     print("Yes,apple is in the fruit tuple")

# tuple length
# myTuple=(1,0,23,54,64)
# print(len(myTuple))


# # index number in tuple
# def create_tuple():
#     fruit=("apple","banana","banana","cherry")
#     print(fruit.count("banana"))
#     print(fruit.index("banana",0,3))
#     print(fruit.index("banana"))
# create_tuple()

# dictionarys 
# list of keys
# x3={1:[11,12,13,14,15,16,17],2:[21,22,23,24,25,26,27],3:[31,32,33,34,35,36,37],4:[41,42,43,44,45,46,47],5:[51,52,53,54,55,56,57],6:[61,62,63,64,65,66,67],7:[71,72,73,74,75,76,77]}
# print(x3.keys())
# # list of values 
# print(x3.values())
# # return value of given key and remove this key
# print(x3.pop(1))
# # remove all item
# print(x3.clear())

# # write a program that scan and email address and forms a tuple of user name and domain
# nemail=int(input("Enter number of email"))
# for i in range(0,nemail):
#     x=str(input("Enter your email address: ")).split("@")
#     s=(x[0])
#     d=(x[1])
#     print('Username :',s)
#     print('Domain :',d)
# # romil code for email verification
# d = {"s@gmail.com":("Romil" , "gmail")}


# email = "1"

# while(not(email == "0")):
#     email = input("Enter your email (0 to exit) : ")
    
#     if(email in d ):
#         print("\n")
#         print(email,"Already exists with the values \nNAME : ",d[email][0],"\nDomain : ",d[email][1],"\n\n")
#     else:
#         domain = email.split("@")
#         while(not(domain[1] == "gmail.com" or domain[1] =="Outlook.com" or domain[1] == "isu.ac.in" or domain[1] == "yahoo.com" or domain[1] == "edu.in")):
#             print("Enter email with following domains only (gmail.com,Outlook.com,isu.ac.in,yahoo.com,edu.in) : ")
#             email = input("\nEnter your email (0 to exit) : ")
#             domain = email.split("@")
            

#         name = input("Enter the name : ")

#         d[email] = (name,domain[1])
# 