

weight_in_kg=int(input("enter weight in kg>"))

height_in_cm=int(input("enter height in cm>"))

height_in_metre=height_in_cm/100

BMI=weight_in_kg/height_in_metre**2

print(BMI)

BMI=round(BMI,2)

print(BMI)