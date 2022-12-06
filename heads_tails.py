#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random
#Write the rest of your code below this line 👇

heads = 1
tails = 0

coinFlip = random.randint(0,1)

if coinFlip == 0:
    print("Tails")
else:
    print("Heads")