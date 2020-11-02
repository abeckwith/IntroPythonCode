import turtle_tasks as tt
import tasks
import turtle  

def main():
    
    input("NOTE: the turtle screen will appear early - "
          " \n don't close it - just move it aside!\n\n"
          "HIT ENTER TO BEGIN\n")
    
    s = turtle.Screen()
    
    # TODO: set up the screen to a size and color of your liking
    
    done = False

    
    while not done:

        print("\nAVAILABLE TASKS: \nSELECT FROM THE FOLLOWING MENU ITEMS: \n"
              "1: Draw a polygon \n"
              "2: Draw random polygons! \n"
              "3: Draw some stairs \n"
              "4: Test if a car has the capacity of 4 others\n"
              "5: (your own title)\n"
              "0: QUIT!\n")
        # TODO: put in the other menu items above for the other functions you write below
        
        selection = int(input("YOUR SELECTION: "))
        
        print() # looks better with a blank line
        
        ####################
        #  turtle tasks:   #
        ####################
        
        if selection == 1: # draw polygon
            num_sides = int(input("How many sides should your polygon have? "))
            side_length = int(input("How long should each side be (in pixels)? "))
            t = turtle.Turtle()
            tt.draw_polygon(t, num_sides, side_length) 
            
        elif selection == 2: # draw random polygons
            # TODO: ask user how many polygons they want and use that variable instead of "5" below:
            # 
            t = turtle.Turtle()
            t.color("blue")
            tt.draw_many_polygons(t, 5) # change 5 to your variable
            
        elif selection == 3: # draw stairs
            #TODO: ask user for number of stairs, make a turtle to send to function
            
            tt.draw_stairs(t, 20, 10) # again, change 20 and 10 to your variables
            
        ########################
        #  non-turtle tasks:   #
        ########################
        elif selection == 4:
            #TODO: ask use for capacities of the 5 cars and use car1, car2, etc.
            can_fit = tasks.four_fit_in_one(car1, car2, car3, car4, car5)
            
            #TODO: process the result of calling the function (also take out "== True"):
            if can_fit == True:
                pass # delete "pass" and tell the user what's up
            else:
                pass # same as abaove
            
            
        #TODO: add more elifs for your functions 
        
        
        
        elif selection == 0: # user has quit
            done = True
    
    
        input("\nHIT ENTER TO CONTINUE")
        
        s.clear() # clear any previous drawings from the turtle Screen before new ones
main()
