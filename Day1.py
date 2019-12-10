import math

import time
now = time.time()

def getModuleFuel(mass) :      

    fuel = math.floor(mass / 3) - 2
    fuel = recursiveFuel(fuel)  
    return fuel

def recursiveFuel(fuel) :
    if fuel < 0 :
        return 0

    fuel = fuel + recursiveFuel(math.floor(fuel / 3) - 2)      
    return fuel

total = 0
with open('Day1Input.txt', 'r') as file :
    for line in file:       
        total += getModuleFuel(int(line))


print(total)
print(time.time() - now)