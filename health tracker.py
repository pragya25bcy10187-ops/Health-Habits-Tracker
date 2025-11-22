def check_water(water):
    if water >=8:
        return"Great job! you drank enough water today."
    else:
        return"Try to drink at least 8 glasses of water."
    
def check_sleep(sleep):
    if sleep>=7:
        return"Nice! You got good sleep."
    else:
        return("Try to get at least 7hr of sleep")
    
def check_BMI(BMI):
    if 18.5<=BMI<=24.9:
        return"Normal, Health Risk is Minimal!"
    elif BMI<18.5:
        return"Underweight ,Health Risk is Minimal!"
    else:
        return"overweigh,Health Risk will increase"
    
def check_BloodPressure(BloodPressure):
    if BloodPressure<120:
        return"Normal"
    elif 120<= BloodPressure<80:
        return"Elevated"
    else:
        return"High"

def check_HeartRate(HeartRate):
    if 60<=HeartRate<=100:
        return"Normal"
    elif HeartRate<60:
        return"Athlete/could be low"
    elif HeartRate>100:
        return"Need attention if frequent"   
    else :
        return"Critical"  
    
     

def check_mood(mood):
    if mood >=7:
        return"you seem to be in good today!"
    else:
        return"take some time for self-care to boost yours mood."     


import csv
from datetime import date


def save_data(data):
    with open ('data.csv','a',newline ='')as file:
        writer= csv.writer(file)
        writer.writerow(data)

def main():
    print("Welcome to Healthy Habits Tracker!")
    water=int(input("Enter glasses of water you drank today:"))
    sleep=float(input('Enter hours of sleep you got last night:'))
    mood=int(input("Enter Rate your mood today(1-10):"))
    BMI=float(input("Enter the BMI"))
    BloodPressure=float(input("Enter the Blood Pressure"))
    HeartRate=int(input("Enter the HeartRate "))

    #check health_goals
    water_feedback=check_water(water)
    sleep_feedback=check_sleep(sleep)
    mood_feedback=check_mood(mood)
    BMI_feedback=check_BMI(BMI)
    BloodPressure_feedback=check_BloodPressure(BloodPressure)
    HeartRate_feedback=check_HeartRate(HeartRate)

    #display feedback
    print(water_feedback)
    print(sleep_feedback)
    print(mood_feedback)
    print(BMI_feedback)
    print(BloodPressure_feedback)
    print(HeartRate_feedback)

    #save data
    today =date.today().isoformat()
    save_data([today,water ,sleep,mood])

if __name__=="__main__":
    main()    

