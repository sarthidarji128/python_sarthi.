# Lists 
# list are mutable
# same subset operation as string


# x=[1,2,3]
# y=x
# x=x+[10,12]
# print(y)
# y.append("hello")
# print(x)
# print(y)


# x=[1,2,3]
# y=x
# z=x
# z=x.append(12)
# x=x+[9,10]1
# print(x)
# print(y)
# print(z)

#tuple 
# x=(1,2,3)
# print(x[1:])
# y=(2,)
# print(y)

# dictionaries is a key value 
# d={1:"HELLO",'sa':[97,12,28,93,10],"sa":{3:"sa",8:12,}}
# print(d['sa'][3])
# del(d["sa"][3])
# print(d)


# questions lab session
# wpp to create list, tuppel, dictionary of seven element. 
# wpp to create tuppels with different data type.
# wpp to arrang list in decending order.
# loop control statement breaks. . . . . . . . . . . . . . . . . . .

# x1=[1,2,3,4,5,6,7]
# x2=['a','b','c','d','e','f','g']
# x3={1:[11,12,13,14,15,16,17],2:[21,22,23,24,25,26,27],3:[31,32,33,34,35,36,37],4:[41,42,43,44,45,46,47],5:[51,52,53,54,55,56,57],6:[61,62,63,64,65,66,67],7:[71,72,73,74,75,76,77]}
# print(x1)
# print()
# print(x2)
# print()
# print(x3[1])
# print(x3[2])
# print(x3[3])
# print(x3[4])
# print(x3[5])
# print(x3[6])
# print(x3[7])


# x={1:'a',2:3.12,3:"SARTHI",4:123,5:"źßk͟h"}
# print(x[1])
# print(x[2])
# print(x[3])
# print(x[4])
# print(x[5])


# shorting the or arrnanging the orders

# l1=[1,2,3,4,5,6,7,8 ] 
# print("Original List:", l1)

# # sorting list using nested loops
# for i in range(0, len(l1)):
# 	for j in range(i+1, len(l1)):
# 		if l1[i] <= l1[j]:
# 			l1[i], l1[j] = l1[j],l1[i]
# print("Sorted List", l1)



# i=1
# for i in range (250):
#     if i==250:
#         break
    
#     else:
#         print(i)
#     i=i+1
    
# manage a liberary catlog use control structures or control statement and maintain the liberary.

books = ["To Kill a Mockingbird","1984","The Great Gatsby","The Catcher in the Rye","Brave New World","One Hundred Years of Solitude","The Lord of the Rings","Pride and Prejudice","The Hobbit","Harry Potter and the Sorcerer's Stone"]
book_cart = []
print("Initial Cart:", book_cart)
print()
print("Book Inventory:", books)
book_cart.append("The Great Gatsby")
print()
book_cart.append("One Hundred Years of Solitude")
print("Updated Cart:", book_cart)
print()
print("Book Inventory:", books)
if "The Great Gatsby" in book_cart:
    book_cart.remove("The Great Gatsby")
print("Final Cart:", book_cart)
print()
print("Book Inventory:", books)
