# 5.Create a program with a list of 10 different names. Use the random module to shuffle the list completely, and then randomly select 3 unique names as the "lottery winners" without repetition.
import random

names = ["a","b","c","d","e","f","g","h","i","k"]
for i in range(3):
    random.shuffle(names)
    name = random.choice(names)
    names.remove(name) 
    print(name)