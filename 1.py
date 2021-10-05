#Advent of code
# 10/4/2021 day1 a and b

filename = "data1.txt"
tickerFile = open(filename)
tickerStr = tickerFile.read()
a_str = tickerStr.split("\n")
modules = [int(i) for i in a_str]
print(modules)
#exit()
maxindex = len(modules)

def fuel_amt(mass):
    fuel = mass//3 - 2
    if fuel > 0:
        return fuel
    else:
        return 0

def part_a():
    fuel = 0
    for mass in modules:
        fuelmod = mass//3 - 2
        fuel += fuelmod
    print(f"day1a fuel = {fuel}")

def part_b():
    fuel = 0
    for mass in modules:
        fuelmod = fuel_amt(mass)
        submass = fuelmod
        while True:
            added_fuel = fuel_amt(submass)
            #print(f"added_fuel={added_fuel}")
            if added_fuel == 0:
                break
            fuelmod += added_fuel
            submass = added_fuel
        fuel += fuelmod
    print(f"day1b fuel = {fuel}")

part_a()
part_b()
    