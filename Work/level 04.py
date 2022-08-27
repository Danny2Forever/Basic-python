#---------22---------
num = int(input())
if num > 0:
    for i in str(num) :
        print(i)
else:
    print("ERROR")

#---------23---------
string = input()
sound = {'a':0 , 'e':0 , 'i':0 , 'o':0 , 'u':0}

total = 0
for index in (string):
    if index == "a":
        sound['a'] += 1
    if index == "e":
        sound['e'] += 1
    if index == "i":
        sound['i'] += 1
    if index == "o":
        sound['o'] += 1
    if index == "u":
        sound['u'] += 1

for j in sound:
    print(f"{j} = {sound[j]}")

#---------24---------
name = input()
charactor = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

if 3 < len(name) < 26 and name[0].lower() in charactor and name[-1:] != "_":
    print("This name can be used.") 
else:
    print("This name cannot be used.") 

#---------25---------
print("---Welcome to Tae Coffee---")
menu = int(input("Please type 1 to show menu: "))
print("---Choose the menu---\n · Espresso\n · Cappucino\n · Latte")
select_ = int(input("Select coffee: "))
 
if select_ == 1:
    select_ = "Espresso"
if select_ == 2:
    select_ = "Cappucino"
if select_ == 3:
    select_ = "Latte"

print("---Choose the type of the coffee---\n · Hot 55 baht\n · Cold 60 baht")
type = int(input("Select type: "))
if type == 1:
    type = "Hot"
    price = 55
if type == 2:
    type = "Cold"
    price = 60

print(f"---You chose {type} {select_} {price}---")

money = int(input("Input your money: "))
change = money - price

while change < 0:
    print("Not enough money please pay more.")
    money += int(input("Input your more money: "))
    change = money - price

print(f"You recieved a change of {change} baht")