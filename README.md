
# ⚖️ BMI Calculator (Python)

## Introduction
This was my very first Python project. 
The purpose of this project is to calculate **Body Mass Index (BMI)** from a user’s height and weight, and classify the result into health categories (underweight, normal, overweight, obese).  

This project helped me learn how to handle user input, perform calculations, and use conditional statements in Python.

---

### The PyCharm script is as follows:
```python
# BMI calculator
name = str(input("Enter your name: "))
weight = float(input("Enter your weight in Kg: "))
height = float(input("Enter your height in M: "))

BMI = weight / height  # note: formula should be weight / (height ** 2)

if BMI <= 18.4:
    print(f"Your BMI is: {BMI} - Underweight")
elif BMI <= 24.9:
    print(f"Your BMI is: {BMI} - Normal")
elif BMI <= 39.9:
    print(f"Your BMI is: {BMI} - Overweight")
elif BMI > 40:
    print(f"Your BMI is: {BMI} - Obese")
else:
    print("Enter valid inputs:")
```
---
## 📚 What I Learned
* Taking user input in Python
* Converting input data types (string → float)
* Basic arithmetic operations
* Writing if / elif / else conditional logic
*Creating a project structure and README for GitHub



    


