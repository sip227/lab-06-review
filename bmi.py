import sys 

print("BMI: Body Mass Index Calculator v0.1 beta")
userWeight = input("Enter your weight(in pounds): ")
userHeight = input("Enter your height (in inches): ")

bmi = (703 * float(userWeight)) / (float(userHeight) * float(userHeight))

print("Your body mass index (BMI) is " + str(bmi) + "%") 





		