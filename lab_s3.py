# list=['sarthi','darji',1,2,33,45]
# print(list)
# for i in range(5):
#     print(i,"-",list[i])
    
# list2=['Ahamdavad','mumbai']
# print(list2)
# print(list2.index('Ahamdavad'))
# print(list2.index('mumbai'))

# list2=['Ahamdavad','mumbai',1,2,34,5,6]
# print(list2)
# print(list2.index('Ahamdavad'))
# print(list2.index('mumbai'))
# print(list2.index(1))
# print(list2.index(2))
# print(list2.index(34))
# print(list2.index(5))

# number=[10,20,30,40,50,60,70,80,90,100]
# print(number[0])
# print(number[3])
# print(number[0:4])
# print(number[-7:4])

# write append to element in list
# numbers=[10,20,30,40,50,60,70,80,90,100]
# print(numbers)
# print(numbers.append(110))
# print(numbers)


# sorting a element of a list print afer msg
# numberss=[10,20,30,40,50,60,70,80,90,100]
# print(numberss)
# numberss.sort(reverse = True)
# print(numberss)


# pop in element list 
# numbersss=[10,20,30,40,50,60,70,80,90,100]
# print(numbersss.pop(1))

# removing
# numberss=[10,20,30,40,50,60,70,80,90,100]
# numberss.remove(30)
# print(numberss)

# numberss.extend([120,130,140,150,160])
# print(numberss)
# numberss.sort(reverse=True)
# print(numberss)

# number=int(input("Total no of element :"))
# mylist=[]
# even=[]
# odd=[]
# for i in range(number):
#     a=int(input("Enter number :"))
#     mylist.append(a)
# print(mylist)
# b=len(mylist)
# for j in range(b):
#     if (mylist[j]%2==0):
#         even.append(mylist[j])
#     else:
#         odd.append(mylist[j])

# print("Even:",even)
# print("odd:",odd)


# wap itrate/traverse a list in a reversed order by three methods using rev ,sliacing,insert

# number=[10,20,30,40,50,60,70,80,90,100]
# print(number)
# number.reverse()
# print("reversed :",number)
# print(number[::-1])

# a=[]
# for i in range(9):
#     a.insert(i,number[i])
    
# print(a)

# wap to extend the list in python by using given approch.

# number=[10,20,30,40,50,60,70,80,90,100]
# print(number)
# number+=[110,120,130]
# print(number)
# number.append([140,150,160])
# print(number)
# number.extend([170,180])
# print(number)


# write a program sum and its mean
# number=[10,20,30,40,50,60,70,80,90,100]
# total=0
# for i in range(9):
#     total+=number[i]
# print("sum :",total)
# total=total/10
# print("mean :",total)



# write a program to remove all duplicates from a list 
# number=[10,20,30,40,50,60,70,80,90,100,1001,10]
# p=len(number)
# a=[]
# for i in range(p):
#     if number[i] not in a:
#         a.append(number[i])
#     else:
#         continue
# print(a)


# x=[[2,5,4],[1,3,9],[7,6,2]]
# y=[[1,8,5],[7,3,6],[4,0,9]]
# sum=[[0,0,0],[0,0,0],[0,0,0]]
# for i in range(len(x)):
#     for j in range(len(y)):
#         sum[i][j]=x[i][j]+y[i][j]
# print(sum)
