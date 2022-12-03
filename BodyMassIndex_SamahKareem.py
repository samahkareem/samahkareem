# BodyMassIndex Project
weight = float(input("enter  weight in pounds"))
height = float(input("enter height in inches'"))

def BMI (weight, height):
    bmi = weight / (height ** 2) * 703
    if (bmi < 18.5):
        return 'You are Underweight',bmi
    elif(bmi >=18.5 and bmi < 24.9) :
        return 'You are Normal ',bmi
    elif (bmi >= 25.0 and bmi < 29.9):
        return 'You are Overweight ',bmi
    elif (bmi >= 30.0):
        return 'You are Obese ',bmi
    else:
        return "Your Vales have error"
qoute, bmi = BMI (weight,height)
print("Your BMI is{},and you are {}".format(bmi,qoute))

