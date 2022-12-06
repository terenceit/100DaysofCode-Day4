# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Generate random number within list bounds
randomName = random.randint(0, len(names)- 1)
#Print name located at random index position
print(f"{names[randomName]} is going to buy the meal today!")