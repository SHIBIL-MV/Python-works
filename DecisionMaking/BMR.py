age=int(input("enter the age :"))

weight=int(input("enter the weight kg:"))

height=int(input("enter the height cm:"))

gender=input("enter the gender: ").lower()

print(weight,height,age,gender)

if gender == "male":

    BMR = 10*weight + 6.25*height - 5*age + 5

elif gender == "female":

    BMR = 10*weight + 6.25*height - 5*age - 161

else:

    print("******please enter valid gener*******")

print(BMR)

activity_level=int(input("""
selet activity level
press 1 for sedentary
press 2 for lightly active
press 3 for moderatly active
press 4 for very active
press 5 for extra active


"""))
if activity_level==1:
    
    calories=BMR*1.2

elif activity_level==2:

    calories=BMR*1.375

elif activity_level == 4:

    calories=BMR* 1.725

elif activity_level==5:

    calories=BMR*1.9

else:
    
    print("select valid choice for activity level *********")
print(f"total number of calories you need in order to maintain your current weight={calories}")


target_weight=int(input("enter weight to reduce in kg :"))

duration=int(input("enter duration in weeks :"))

# 1kg => 7700

calories_defict=target_weight*7700

days=duration*7

daily_calorie_defi=calories_defict/days

print("daily_calorie_defict",daily_calorie_defi)