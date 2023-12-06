num = int(input("Enter the number :"))
sum = 0
if num<=0:
      print("invalid number")
else:
      for i in range(1,num+1):
            print(i)
            sum=sum+i
print()
print("The sum of the number :-",sum)