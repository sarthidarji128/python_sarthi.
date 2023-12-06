rows = 3
for i in range(rows):
    for k in range(i-2, rows):
        print(chr(65 + k+2), end=" ")
        print() 
       
for s in range(rows):
    for h in range(s):
        print("", end=" ")
    for s in range(i-2, rows):
        print(chr(65 + s+2), end=" ")
print()
        
        