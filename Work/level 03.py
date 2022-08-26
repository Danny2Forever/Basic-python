#---------18---------
w = float(input("Weight (kg): "))
h = float(input("Height (m): "))
bmi = w/h**2
print(f"BMI is {bmi}")
if bmi < 18.5 :
    print("Underweight")
elif bmi < 25 :
    print("Nomal weight")
elif bmi < 30 :
    print("Overweight")
elif bmi >= 30 :
    print("Obesity")

#---------19---------
username = input("Username: ")
password = input("Password: ")
User = "admin"
Pass = "Ad13n@23t"

if username == User and password == Pass :
    print("Welcome. admin")
else :
    print("You are not admin")

#---------18 - 21---------
x = ["dog", "cat", "hamster"]
#---18---
x.append("snake")
print(x)

#---19---
x.insert(1, "bird")
print(x)

#---20---
x.pop()
print(x)

#---21---
x.remove("dog")
print(x)