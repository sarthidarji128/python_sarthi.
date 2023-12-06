# printing horizotally


# sarthi=['1','2','3','4']
# for i in sarthi:
#     print(i,end="/")
# print('12','08','2006', sep="/")


  
# Merging Dictionary



# method 1 using ( | )

# l1={'sarthi':17,'chaitali':16}
# l2={'hemang':16,'hardik':18}
# mainlist=l1|l2
# print(mainlist)

# method 2 using ( **listname,another **list name  )
# l1={'sarthi':17,'chaitali':16}
# l2={'hemang':16,'hardik':18}
# l3={**l1,**l2}
# print(l3)



# calender with python 



# year 2023

# import calendar
# n=1
# x=13
# for i in range(n,x):
#     month=calendar.month(2023,i)
#     print(month)

# using calender im finding the year is leap  or not 

# import calendar
# year=int(input("enter the year to check year is leap or not a leap year :"))
# month=calendar.isleap(year)
# if month==True:
#     print(year," is leap year")
# else:
#     print(year," is not a leap year")



# Get current date and time 

# from datetime import datetime
# time_now=datetime.now().strftime('%H:%M:%S')
# print(f'the time now if {time_now}')

# # import date  using date proper
# from datetime import date
# todayd=date.today()
# print(todayd)



# sort a list in decending order


# number=[1,2,3,4,5,6,7,8,9]
# number.sort(reverse=True)
# print(number)



# Swapping variables 


# method 1

# x=int(input("enter the value of x :"))
# y=int(input("enter the value of y :"))
# x,y=y,x
# print("Swapping the variable......")
# print('x is',x)
# print('y is',y)

# method 2 xor method 

# x=10
# y=20
# x^=y
# y^=x
# x^=y
# print(x)
# print(y)



# counting item occuurences

# using inbuilt dictionary

# from collections import Counter
# list1=['sarthi','sarthi','darji','sarthi']
# n=Counter(list1).get('darji')
# print(n)

# using normal loop methods

# list1=['sarthi','sarthi','darji','sarthi']
# count=0
# for i in list1:
#     if i=='sarthi':
#         count+=1
# print(count)



# Flatten a nested list 
# m1
# list1=[[1,2,3],[4,5,6]]
# newlist=[]
# for i in list1:
#     for j in i:
#         newlist.append(j)
# print(newlist)

# m2 using itertools

# import itertools
# l=[1,2,3],[4,5,6]
# l2=list((itertools.chain.from_iterable(l)))
# print(l2)

# m3using list comprehension

# l1=[[1,2,3],[4,5,6]][]
# l2=[i for j in l1 for i in j]
# print(l2)



# Index of biggest number 
# x=[10,20,30,40,50,60,70,80,90,100]
# max=max(enumerate(x,start=0),key=lambda x:x[1])
# print(max)




# Absolute value of a n 

# n=[-12,-23,-53,-56]
# print([abs(i) for i in n])

# n=-233
# print(abs(n))

# complex number accurate value 
# c=6+3j
# print(abs(c))





# Adding thousandd operators of a number

# a=[1000000,200000,300000]
# n=['{:,}'.format(i) for i in a]
# print(n)




# Startwith and endwith methods 
# startwith

# n=['apple','orange','lemon','apricot']
# s=[i for i in n if i.startswith('a')]
# print(s)

# endwith

# n=['apple','orange','lemon','apricot']
# s=[i for i in n if i.endswith('e')]
# print(s)




# Nlargest and Nsmallest

# nlargest

# import heapq
# s=[1,2,3,4,5,6,7,8,9,10]
# print(heapq.nlargest(5,s))

# nSmallest 

# import heapq
# s=[1,2,3,4,5,6,7,8,9,10]
# print(heapq.nsmallest(5,s))




# checking Anagram 
# using inbuilt library

# from collections import Counter
# a='sarthi'
# b='ihtrsa'
# print(Counter(a)==Counter(b))

# using normal methods

# a='lost'
# b='stol'
# if sorted(a)==sorted(b):
#     print("Anagrams")
# else:
#     print("not a anagram")




# Properties and methods 

# a="i love c++"
# print(dir(a))




# Open A website using pyhton
# import webbrowser
# url='https://www.youtube.com/watch?v=vC73sFPIFzU&t=3184s'
# o=webbrowser.open(url)
# print(o)

# 19
import webbrowser
url='https://www.geeksforgeeks.org/how-to-install-pip-in-macos/'
o=webbrowser.open(url)
print(o)