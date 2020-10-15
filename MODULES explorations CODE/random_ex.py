import random

print("random integers between 1000 and 2000 (numbers could repeat):")
for i in range(10):
    print(random.randint(1000, 2000))
print("")

print("random floats >=0 and < 1 (numbers could repeat):")
for i in range(10):
    print(random.random()) 
print("")

print("random numbers between 4 and 11 (numbers could repeat):")
for i in range(10):  
    print(random.randint(4, 11)) 
print("")

print("shuffles values, so NO REPEATS:")
nums = ["1st", "2nd", "3rd", "4th"] 
for i in range(4):
    random.shuffle(nums)        
    print(nums)

'''
ASSIGNMENT:
   1. Write code that will ask the user for a min, a max, and a number n.
      Your code will display n random numbers between min and max
    2.  Write code that will randomly select from a hat 3 colored pieces of paper
     (once a given piece is selected, it shouldn't be possible to select again),
     Display the results by just showing the colors and the order
     they were selected.
     Assume that the hat has 3 red, 2 green, 2 purple, 1 yellow, and 1 orange
     piece of paper

   3. Write code that will print 20 random numbers between 1 and 1000, but skewed towards
     100, so that high numbers are rare, but will still appear
'''