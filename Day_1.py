#first program of python
a = 3
b = 2
print(a,"+",b,"=",a+b) 
print(a,"-",b,"=",a-b)
print(a,"X",b,"=",a*b)
print(a,"/",b,"=",a/b)
print("hello world")
fname='Welcome'
lname='B Tech'
print(fname,lname)
print()

# operator overloading
x="hello"
x=x + " how are you ?"
print (x)
s="""how are you ?\n heyyy🔥"""
print(s)
print()
print()

# understanding substring and methods 
# len(String)- return the number of characters in the String 
# str(Object)- return a string representation of the object 
print(s[:4])
print(s[4:13])
print(s[-2])
print(s[:2])
print()
print()


# string Formating
print("one,%d,three"%(2))
print()
print()


# list
# order collection of data 
# Data can be of different type 
# List are mutable (contain can change without their identify)
# Same subset operaton as string 
# x[i]=a
# the method append also modifies 
# x.append('value')

d=['sarthi','darji','sanjaybhai']
d.append("🔥")
print(d)
f=d
d[1]="DARIJ"
print(f[0],f[2],f[1])
print()
# another method
# the method append modifies the list and return none
# List addition (+) return a new list 
# x=x+[value]
g=d.append(1)
print(g==None)
d=d+['hey bro']
print(d)
g=d+['!!']
print(g)
print()


# tuples 
# Tuple are immunable version
# in (value,)

n=(1,2,3)
print(n[1:])
print()

# Dictionaries
# set of keys value pairs
# Dictionaries are mutable 
# x={1:'hello','two':3,}
# d['two']
# 3

b={1:'hello',2:'how are you ?',3:'i am fine'}
print(b)
# modified list
b[2]='hii'
print(b)
print()

# delet method 
# del(d[2])
del(b[2])
print(b)
print()

# copying dict and list
# list are ditto copy
l1=[1]
l2=list(l1)
l1[0]=10
print(l1)
print(l2)
print()
print()


# copy and modifies
# d={1:10}
# d2=d.copy()
# d[1]=22

d={1:10}
d2=d.copy()
d[1]=22
print(d2)
print(d)
print()
