age=int(input("Enter your age:"))
if age < 5:
    print("Free")
elif 5 <= age < 17:
    print("$10")
elif 18 <= age <= 64:
    print("$20")
elif age >=65:
    print("$15")
else:
    print("Invalid age")