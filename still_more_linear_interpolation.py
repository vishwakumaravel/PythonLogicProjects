# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Vishwa Kumaravel
#        Diego Reyes
# Section: 579
# Assignment: Lab 3.16
# Date: 9/7/2023
#
import math

#Inputs
t1 = float(input("Enter time 1: "))
x1 = float(input("Enter the x position of the object at time 1: "))
y1 = float(input("Enter the y position of the object at time 1: "))
z1 = float(input("Enter the z position of the object at time 1: "))
t2 = float(input("Enter time 2: "))
x2 = float(input("Enter the x position of the object at time 2: "))
y2 = float(input("Enter the y position of the object at time 2: "))
z2 = float(input("Enter the z position of the object at time 2: "))
rnd_t1 = "{:.2f}".format(t1)
rnd_t2 = "{:.2f}".format(t2)

#time 1/5
slope = (x2-x1)/(t2-t1)
x = float(slope*(t1-t1) + x1)
rnd_x = "{:.3f}".format(x)
slope1 = (y2-y1)/(t2-t1)
y = float(slope1*(t1-t1) + y1)
rnd_y = "{:.3f}".format(y)
slope2 = (z2-z1)/(t2-t1)
z = float(slope2*(t1-t1) + z1)
rnd_z = "{:.3f}".format(z)
print(f"At time {rnd_t1} seconds the object is at ({rnd_x} , {rnd_y}, {rnd_z})")

#time 2/5
time = t1 + ((t2-t1)/4)
rnd_time = "{:.2f}".format(time)
x = float(slope*(time-t1) + x1)
rnd_x = "{:.3f}".format(x)
y = float(slope1*(time-t1) + y1)
rnd_y = "{:.3f}".format(y)
z = float(slope2*(time-t1) + z1)
rnd_z = "{:.3f}".format(z)
print(f"At time {rnd_time} seconds the object is at ({rnd_x} , {rnd_y}, {rnd_z})")

#time 3/5
time = time + ((t2-t1)/4)
rnd_time = "{:.2f}".format(time)
x = float(slope*(time-t1) + x1)
rnd_x = "{:.3f}".format(x)
y = float(slope1*(time-t1) + y1)
rnd_y = "{:.3f}".format(y)
z = float(slope2*(time-t1) + z1)
rnd_z = "{:.3f}".format(z)
print(f"At time {rnd_time} seconds the object is at ({rnd_x} , {rnd_y}, {rnd_z})")

#time 4/5
time = time + ((t2-t1)/4)
rnd_time = "{:.2f}".format(time)
x = float(slope*(time-t1) + x1)
rnd_x = "{:.3f}".format(x)
y = float(slope1*(time-t1) + y1)
rnd_y = "{:.3f}".format(y)
z = float(slope2*(time-t1) + z1)
rnd_z = "{:.3f}".format(z)
print(f"At time {rnd_time} seconds the object is at ({rnd_x} , {rnd_y}, {rnd_z})")

#time 5/5
time = time + ((t2-t1)/4)
rnd_time = "{:.2f}".format(time)
x = float(slope*(time-t1) + x1)
rnd_x = "{:.3f}".format(x)
y = float(slope1*(time-t1) + y1)
rnd_y = "{:.3f}".format(y)
z = float(slope2*(time-t1) + z1)
rnd_z = "{:.3f}".format(z)
print(f"At time {rnd_time} seconds the object is at ({rnd_x} , {rnd_y}, {rnd_z})")
