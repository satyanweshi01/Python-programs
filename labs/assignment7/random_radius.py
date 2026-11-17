# 4.Write a script that generates a random floating-point number between 5.0 and 15.0 to represent the radius of a circle. Use the math module to calculate and print the circle's area and circumference.4.Write a script that generates a random floating-point number between 5.0 and 15.0 to represent the radius of a circle. Use the math module to calculate and print the circle's area and circumference.
import random
import math

random_radius = random.uniform(5.0,15.0)

area = random_radius*(math.pi)**2
cir = 2*math.pi*random_radius

print("Area :", area, "Circumference :", cir)