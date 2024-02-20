# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Vishwa Kumaravel
#        Diego Reyes
# Section: 579
# Assignment: Lab 4.13
# Date: 9/10/2023
#


#inputs
pay = float(input("How much did you pay?"))
cost = float(input("How much did it cost?"))

#defining variables
change = round(100*(pay - cost))
q = 0
d = 0
n = 0
p = 0

#conditions
if(change % 25 == 0):
    q = change//25
    d = 0
    n = 0
    p = 0
elif((change - ((int(change//25)*25))%10) == 0):
    q = int(change//25)
    d = int((change - (q*25))//10)
    n = 0
    p = 0
elif((change - (int(change//25)*25) - ((int(change//25//10)*10))%5) == 0):
    q = int(change//25)
    d = int((change - (q*25))//10)
    n = int((change - q*25 - d*10)//5)
    p = 0
else:
    q = int(change//25)
    d = int((change - (q*25))//10)
    n = int((change - q*25 - d*10)//5)
    p = int(change - q*25 - d*10 - n*5)
    

#prints  
print(f"You received ${float(change/100):0.2f} in change. That is...")
if(int(q) != 0 and int(q) != 1 ):
    print(f"{q:.0f} quarters")
elif(int(q) == 1):
    print(f"{1:.0f} quarter")
if(int(d) != 0 and int(d) != 1 ):
    print(f"{d:.0f} dimes")
elif(int(d) == 1):
    print(f"{1:.0f} dime")
if(int(n) != 0 and int(n) != 1 ):
    print(f"{n:.0f} nickels")
elif(int(n) == 1):
    print(f"{1:.0f} nickel")
if(int(p) != 0 and int(p) != 1 ):
    print(f"{p:.0f} pennies")
elif(p == 1):
    print(f"{1:.0f} penny")