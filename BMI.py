 #BMI calculator
name= str(input("Enter your name: "))
weight= float (input("Enter your weight in Kg: "))
height= float(input("Enter your height in M: "))
BMI= weight/height
if BMI <= 18.4:
    print(f"Your BMI is: {BMI}-underweight")
elif BMI<= 24.9:
    print(f'Your BMI is: {BMI} - Normal')
elif BMI <=39.9:
    print(f"Your BMI is : {BMI}- Overweight ")
elif BMI >40:
    print(f"Your BMI is : {BMI}- Obese ")
else:
    print("Enter valid inputs:")

