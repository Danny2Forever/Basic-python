#---------5--------- 
base = float(input("Enter base : "))
high = float(input("Enter high : "))
print((base*high)/2)

#---------6--------- 
C = float(input("Enter C : "))
F = (C*9)/5+32
K = C + 273.15
print(f"{F} {K}")

#---------7--------- 
a = int(input())
b = int(input())
print("Addition: "+str(a+b))
print("Concatenation: "+str(a)+str(b))


#---------8--------- 
import math
a = int(input())
print(int(math.fabs(a)))

#---------9---------
import math
a = float(input())
a = math.fabs(a)
a = math.ceil(a)
print(a*-1)

#---------10---------
a = int(input("Enter a : "))
while a <= 0 :
    a = int(input("Enter a : "))
if a < 90 :
    print("a > 90")
else: 
    print("a !> 90")

#---------11---------
a = int(input("Enter a : "))
while a <= 0 :
    a = int(input("Enter a : "))
if a % 3 == 0:
    print("a divisible 3")
else:
    print("a indivisible 3")

#---------12---------
num = []
for i in range(3):
    a = int(input(f"({i}) Enter number : "))
    num.append(a)
print("The max : ",max(num))

#---------13---------
#---13.1---
i = 1
while i <= 15:
    print(f"{i}, ",end="")
    i += 2
print("Stop at 15")

#---13.2---
i = 2
while i <= 17:
    print(f"{i}, ",end="")
    i += 3
print("Stop at 17")

#---13.3---
i = 30
while i >= -30 :
    if i == -30 :
        print(f"{i} ",end="")
    else:
        print(f"{i}, ",end="")
    i -= 10
print("Stop at -30")