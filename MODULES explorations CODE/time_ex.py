import time

# saves the current time in seconds into the variable start_time:
start_time = time.time()  

for i in range(200):
    print(i)

# subtract start time from end time to get elapsed time
end_time = time.time()
elapsed_time = end_time - start_time 
                         
print("Well, that took ", elapsed_time, "seconds!")

'''
ASSIGNMENT:
    1.  Run the above code in IDLE, Thonny, and Terminal* and record the results
    in the blanks below
   
   *To run in terminal, at the "$" prompt, type "python3 " (that's a space after
   the 3) then find this .py file in Finder and drag it to terminal and hit ENTER
       
   QUESTION: How long did it take to run in each of the 3 environments?
   WRITE THE VALUES HERE:
   
   IDLE: __________ Thonny: _________  Terminal: ___________

 2.  Write code that will ask the user three times in a row to simply hit ENTER
     (use three input()'s or use a for loop)
     
     Display how long it took them from the first enter to the last enter - you
     can use the same idea as the above code in lines 4, 10 and 11

 NOTE: any game you write could have a time component where players get more
  points for getting through more quickly...
'''


