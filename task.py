# print h
# print("Hello"[0])

# print last character
# print("Hello"[-1])

# interger = whole number
# print(123 +345)

# large integer
# print(123_456_789)

# float
# print(3.14)

# boolean
# print(True)
# print(False)

#data type
# print(type(1))
# print(type("string"))
# print(type(3.14))
# print(type(True))


# type conversion
# print(int("1") + int("2"))

# print("Number of letters in your name " + str(len(input("Enter your name"))))

# 1+1 , 7-3, 3*2, 6/3, 5//3, 2 ** 2


# ****************************
# BMI CALC weight / height **2

# weight = float(input("weight: "))
# height = float(input("height: "))

# BMI = weight /height ** 2
# print("BMI: " + str(BMI))

# print(round(BMI))
# print(round(BMI, 2))
# ******************************

#  f-string
# score = 0
# height = 1.8
# is_winning = True

# print(f"Your score is {score}. Your height is {height}. You are winning is {is_winning}.")

# CALCULATOR
# 

print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people are splitting the bill? "))

bill_total = round((total + (tip/100 * total))/number_of_people , 2)

print(f"Each person should pay: ${bill_total}")