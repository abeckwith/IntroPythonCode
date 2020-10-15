# Math module exploration

import math

print("FACTORIALS:")

# NOTE: n! = n factorial = n * (n - 1) * (n - 2)....* 3 * 2 * 1
factors = "= "
for num in range(1, 20):
    if num == 1:
        factors = factors + str(num)
    else:
        factors = factors + "*" + str(num) 
        
    print(math.factorial(num), factors) # uses the math.factorial function

print("\nSQUARE ROOTS")
for num in range(1, 26):
    print(math.sqrt(num))         # uses the math.sqrt function

print("\npi:")
print(math.pi)                    # uses the math.pi constant

print("\nsin of pi/2 and 3pi/2:")
print(math.sin(math.pi / 2))      # combo of sine and pi
print(math.sin(3 * math.pi / 2))


''' 
ASSIGNMENT:
1. write code where the user enters a START and END number and you print out 
 the square root and the factorial of each of the numbers between those two
 (use a for loop)

2. Write code that asks the user for the length of a pendulum and the force
due to gravity.  

Your code will calculate how long it takes for the pendulum to swing once,
using the formula:    
  two times pi times the square root of the length (in meters) divided by the 
  force due to gravity (NOTE: length / force is all under the square root)

(YOU MUST USE THE π VALUE FOUND IN THE MATH MODULE - DON'T USE 3.14)

To test your code:
• a length of 1.5 meters and Earth's gravity of 9.8 should 
result in a swing time of about 2.5 seconds
• a super long pendulum of 10 meters on Mars (gravity there is 3.711 m/s/s)
should result in a swing time of about 10.31 seconds)


'''
