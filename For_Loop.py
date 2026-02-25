# 1.Dice Rolling Simulation
import random

rolls = 20
count_6 = 0
count_1 = 0
two_6_row = 0
previous_roll = 0

for i in range(rolls):
    roll = random.randint(1, 6)
    print("Roll", i+1, ":", roll)

    if roll == 6:
        count_6 += 1
        if previous_roll == 6:
            two_6_row += 1
    if roll == 1:
        count_1 += 1

    previous_roll = roll

print("\nStatistics:")
print("Number of times rolled 6:", count_6)
print("Number of times rolled 1:", count_1)
print("Number of times rolled two 6s in a row:", two_6_row)

print("*********************************************")

# 2.Jumping Jack Workout Program
total_jumping_jacks = 100
completed = 0

for i in range(1, 11):  # 10 sets of 10
    print("\nPerform 10 jumping jacks")
    completed += 10

    if completed == 100:
        print("Congratulations! You completed the workout.")
        break

    tired = input("Are you tired? (yes/y or no/n): ").lower()

    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").lower()
        if skip in ["yes", "y"]:
            print("You completed a total of", completed, "jumping jacks.")
            break
        else:
            print(total_jumping_jacks - completed, "jumping jacks remaining.")
    else:
        print(total_jumping_jacks - completed, "jumping jacks remaining.")
