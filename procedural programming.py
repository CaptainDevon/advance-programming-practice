#code for demonstration of procedural programming
#factorial of a given number
def fact(n):
    if n==0:
        return 1

    else:
        return n*fact(n-1)

a=int(input("enter the value to find factorial for:"))
result=fact(a)
print(result)

print("Name:Divyansh Sinha")
print("RegNo:RA2111026030117")
print("section:C")


