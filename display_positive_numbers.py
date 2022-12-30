 #to accept a list and display all positive numbers
l=[]
n=int(input("Enter number of elements you want in the list : "))
for i in range(n):
    a=int(input("Enter an element : "))
    l.append(a)
print(l)
for i in range(len(l)):
    if l[i]>0:
        print(l[i],end=" ")
 
