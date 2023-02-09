# dice rolling app
import random

def Roll_Stats_3d6():
    numberOfStats = 6
    for i in range(numberOfStats):
        Roll_1 =(random.randint(1, 6))
        Roll_2 =(random.randint(1, 6))
        Roll_3 =(random.randint(1, 6))
        Total = Roll_1 + Roll_2 + Roll_3
        print("You rolled a " + str(Total))


def Roll_Custom_Dice():
    numberOfDice = int(input("How many dice do you want to roll? "))
    numberOfSides = int(input("How many sides should each die have? "))
    for i in range(numberOfDice):
        (print(random.randint(1, numberOfSides)))

def Roll_4d6_Droplow():
    numberOfStats = 6
    for i in range(numberOfStats):
        rolls = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
        #print(rolls)
        rolls.remove(min(rolls))
        total = sum(rolls) #adds rolls together, just declaring sum(rolls), then printing rolls fails
        print(total)

#Roll_Custom_Dice()
#Roll_Stats_3d6()
#Roll_4d6_Droplow()

