import random

def roll_dice(sides, rolls):
    for roll in range(rolls):
        print(f"Roll {roll+1}: {random.randint(1, sides)}")

def main():
    sides = int(input("Enter the number of sides on the dice: "))
    rolls = int(input("Enter the number of rolls: "))
    
    roll_dice(sides, rolls)

if __name__ == "__main__":
    main()