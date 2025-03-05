n=int(input("enter the no of row:"))
for i in range(n):#for row
    for j in range(n-i-1):#for colomn space
        print(" ",end="")
    for j in range(i+1):#for coloumn star
        print("*", end=" ")
    print()# for newline
    
input()