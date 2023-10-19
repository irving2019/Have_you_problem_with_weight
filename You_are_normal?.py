def bmi(height, weight):
    bmi2 = height/(weight**2)
    if bmi2 <= 18.5:
        print("Underweight")
    elif bmi2 <= 25.0:
        print("Normal")
    elif bmi2 <= 30.0:
        print("Overweight")
    else:
        print("Obese")
