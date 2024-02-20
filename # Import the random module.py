# Import the random module
import random

# Define possible values and ranges
sex_vals = ["F", "M"]
age_vals = range(20, 79)
cho_vals = range(100, 300)
smo_vals = ["Y", "N"]
hdl_vals = range(20, 80)
sbp_vals = range(80, 200)
med_vals = ["Y", "N"]
test_cases = []

# Generate and print test cases one by one
for _ in range(250):  # Adjust the number of test cases as needed
    sex = random.choice(sex_vals)
    age = random.choice(age_vals)
    cho = random.choice(cho_vals)
    smo = random.choice(smo_vals)
    hdl = random.choice(hdl_vals)
    sbp = random.choice(sbp_vals)
    med = random.choice(med_vals)
    
    
    # Calculate points and risk based on your provided logic
    points = 0
    risk = ""

    if(sex == "F"):

        # AGE POINTS #

        if( 20 <= age <= 34):
            points += -7
        elif( 35 <= age <= 39):
            points += -3
        elif( 40 <= age <= 44):
            points += 0
        elif( 45 <= age <= 49):
            points += 3
        elif( 50 <= age <= 54):
            points += 6
        elif( 55 <= age <= 59):
            points += 8
        elif( 60 <= age <= 64):
            points += 10
        elif( 65 <= age <= 69):
            points += 12
        elif( 70 <= age <= 74):
            points += 14
        elif( 75 <= age <= 79):
            points += 16

        # Cholestrol POINTS #

        #row 1
        if(cho < 160):
            points += 0

        #row2
        elif(159 < cho < 200 and 20 <= age <= 39):
            points += 4
        elif(159 < cho < 200 and 40 <= age <= 49):
            points += 3
        elif(159 < cho < 200 and 50 <= age <= 59):
            points += 2
        elif(159 < cho < 200 and 60 <= age <= 69):
            points += 1
        elif(159 < cho < 200 and 70 <= age <= 79):
            points += 1

        #row 3
        elif(199 < cho < 240 and 20 <= age <= 39):
            points += 8
        elif(199 < cho < 240 and 40 <= age <= 49):
            points += 6
        elif(199 < cho < 240 and 50 <= age <= 59):
            points += 4
        elif(199 < cho < 240 and 60 <= age <= 69):
            points += 2
        elif(199 < cho < 240 and 70 <= age <= 79):
            points += 1

        #row 4
        elif(239 < cho < 280 and 20 <= age <= 39):
            points += 11
        elif(239 < cho < 280 and 40 <= age <= 49):
            points += 8
        elif(239 < cho < 280 and 50 <= age <= 59):
            points += 5
        elif(239 < cho < 280 and 60 <= age <= 69):
            points += 3
        elif(239 < cho < 280 and 70 <= age <= 79):
            points += 2

        #row 5
        elif(cho >= 280 and 20 <= age <= 39):
            points += 13
        elif(cho >= 280 and 40 <= age <= 49):
            points += 10
        elif(cho >= 280 and 50 <= age <= 59):
            points += 7
        elif(cho >= 280 and 60 <= age <= 69):
            points += 4
        elif(cho >= 280 and 70 <= age <= 79):
            points += 2

        #Smoker Points#

        #row 1
        if(smo == "N"):
            points += 0

        #row2
        elif(smo == "Y" and 20 <= age <= 39):
            points += 9
        elif(smo == "Y" and 40 <= age <= 49):
            points += 7
        elif(smo == "Y" and 50 <= age <= 59):
            points += 4
        elif(smo == "Y" and 60 <= age <= 69):
            points += 2
        elif(smo == "Y" and 70 <= age <= 79):
            points += 1

        #HDL points#
        if(hdl >= 60):
            points+=-1
        elif( 50 <= hdl <= 59):
            points+=0
        elif( 40 <= hdl <= 49):
            points+=1
        elif( hdl < 40):
            points+=2

        #SBP points#

        #row 1
        if(sbp < 120):
            points+= 0

        #row2
        elif(120 <= sbp <= 129 and med == "N"):
            points += 1
        elif(120 <= sbp <= 129 and med == "Y"):
            points += 3

        #row3
        elif(130 <= sbp <= 139 and med == "N"):
            points += 2
        elif(130 <= sbp <= 139 and med == "Y"):
            points += 4

        #row4
        elif(140 <= sbp <= 159 and med == "N"):
            points += 3
        elif(140 <= sbp <= 159 and med == "Y"):
            points += 5

        #row3
        elif(sbp >= 160 and med == "N"):
            points += 4
        elif(sbp >= 160 and med == "Y"):
            points += 6

        #point total#
        if(points < 9):
            risk = "<1"
        elif(9 <= points <= 12):
            risk = "1"
        elif(13 <= points <= 14):
            risk = "2"
        elif(points == 15):
            risk = "3"
        elif(points == 16):
            risk = "4"
        elif(points == 17):
            risk = "5"
        elif(points == 18):
            risk = "6"
        elif(points == 19):
            risk = "8"
        elif(points == 20):
            risk = "11"
        elif(points == 21):
            risk = "14"
        elif(points == 22):
            risk = "17"
        elif(points == 23):
            risk = "22"
        elif(points == 24):
            risk = "27"
        elif(points >= 25):
            risk = ">30"



    if(sex == "M"):
        # AGE POINTS #

        if( 20 <= age <= 34):
            points += -9
        elif( 35 <= age <= 39):
            points += -4
        elif( 40 <= age <= 44):
            points += 0
        elif( 45 <= age <= 49):
            points += 3
        elif( 50 <= age <= 54):
            points += 6
        elif( 55 <= age <= 59):
            points += 8
        elif( 60 <= age <= 64):
            points += 10
        elif( 65 <= age <= 69):
            points += 11
        elif( 70 <= age <= 74):
            points += 12
        elif( 75 <= age <= 79):
            points += 13

        # Cholestrol POINTS #

        #row 1
        if(cho < 160):
            points += 0

        #row2
        elif(159 < cho < 200 and 20 <= age <= 39):
            points += 4
        elif(159 < cho < 200 and 40 <= age <= 49):
            points += 3
        elif(159 < cho < 200 and 50 <= age <= 59):
            points += 2
        elif(159 < cho < 200 and 60 <= age <= 69):
            points += 1
        elif(159 < cho < 200 and 70 <= age <= 79):
            points += 0

        #row 3
        elif(199 < cho < 240 and 20 <= age <= 39):
            points += 7
        elif(199 < cho < 240 and 40 <= age <= 49):
            points += 5
        elif(199 < cho < 240 and 50 <= age <= 59):
            points += 3
        elif(199 < cho < 240 and 60 <= age <= 69):
            points += 1
        elif(199 < cho < 240 and 70 <= age <= 79):
            points += 0

        #row 4
        elif(239 < cho < 280 and 20 <= age <= 39):
            points += 9
        elif(239 < cho < 280 and 40 <= age <= 49):
            points += 6
        elif(239 < cho < 280 and 50 <= age <= 59):
            points += 4
        elif(239 < cho < 280 and 60 <= age <= 69):
            points += 2
        elif(239 < cho < 280 and 70 <= age <= 79):
            points += 1

        #row 5
        elif(cho >= 280 and 20 <= age <= 39):
            points += 11
        elif(cho >= 280 and 40 <= age <= 49):
            points += 8
        elif(cho >= 280 and 50 <= age <= 59):
            points += 5
        elif(cho >= 280 and 60 <= age <= 69):
            points += 3
        elif(cho >= 280 and 70 <= age <= 79):
            points += 1

        #Smoker Points#

        #row 1
        if(smo == "N"):
            points += 0

        #row2
        elif(smo == "Y" and 20 <= age <= 39):
            points += 8
        elif(smo == "Y" and 40 <= age <= 49):
            points += 5
        elif(smo == "Y" and 50 <= age <= 59):
            points += 3
        elif(smo == "Y" and 60 <= age <= 69):
            points += 1
        elif(smo == "Y" and 70 <= age <= 79):
            points += 1

        #HDL points#
        if(hdl >= 60):
            points+=-1
        elif( 50 <= hdl <= 59):
            points+=0
        elif( 40 <= hdl <= 49):
            points+=1
        elif( hdl < 40):
            points+=2

        #SBP points#

        #row 1
        if(sbp < 120):
            points+= 0

        #row2
        elif(120 <= sbp <= 129 and med == "N"):
            points += 0
        elif(120 <= sbp <= 129 and med == "Y"):
            points += 1

        #row3
        elif(130 <= sbp <= 139 and med == "N"):
            points += 1
        elif(130 <= sbp <= 139 and med == "Y"):
            points += 2

        #row4
        elif(140 <= sbp <= 159 and med == "N"):
            points += 1
        elif(140 <= sbp <= 159 and med == "Y"):
            points += 2

        #row5
        elif(sbp >= 160 and med == "N"):
            points += 2
        elif(sbp >= 160 and med == "Y"):
            points += 3

        #point total#
        if(points < 0):
            risk = "<1"
        elif(0 <= points <= 4):
            risk = "1"
        elif(5 <= points <= 6):
            risk = "2"
        elif(points == 7):
            risk = "3"
        elif(points == 8):
            risk = "4"
        elif(points == 9):
            risk = "5"
        elif(points == 10):
            risk = "6"
        elif(points == 11):
            risk = "8"
        elif(points == 12):
            risk = "10"
        elif(points == 13):
            risk = "12"
        elif(points == 14):
            risk = "16"
        elif(points == 15):
            risk = "20"
        elif(points == 16):
            risk = "25"
        elif(points >= 17):
            risk = ">30"

        # Append the test case to the list with risk category
    test_cases.append(f"sex:{sex} age:{age} cho:{cho} smo:{smo} hdl:{hdl} sbp:{sbp} med:{med} out:{risk}")

# Shuffle the test cases to randomize the order
random.shuffle(test_cases)

# Print the test cases
for test_case in test_cases:
    print(test_case)