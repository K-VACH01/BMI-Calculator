print("BMI CALCULATOR")

name = input("Enter your name: ")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))

height_m = height / 100
bmi = weight / (height_m * height_m)
bmi = round(bmi, 2)

print("Your BMI is:", bmi)

if bmi < 18.5:
    print("You are Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("You are Normal weight")
elif bmi >= 25 and bmi < 30:
    print("You are Overweight")
else:
    print("You are Obese")

print("Thank you", name)