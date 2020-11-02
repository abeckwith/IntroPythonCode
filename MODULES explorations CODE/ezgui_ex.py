'''
First, INSTALL EASYGUI, using terminal:

$ pip3 install easygui
or in Thonny: Tools, Manage Plugins, search for easygui, click Install
'''
# NOW RUN THIS CODE TO SEE HOW IT WORKS...

import easygui

    # messagebox:
easygui.msgbox(msg="Click OK to begin!", title="Start Screen")
easygui.msgbox(msg="Are you ready?", title="Start Screen", 
                                        ok_button="Yes!")
# NOTE: default text for ok_button is "OK"



   # get text from user:
name = easygui.enterbox(msg="What is your name?", title="Get Info")
color = easygui.enterbox(msg="What is your favotire color?", title="Get color", 
                                       default="(type color here)")
easygui.msgbox(msg="Hello " + name)



   # continue/cancel & yes/no boxes:
answer = easygui.ccbox(msg="Go to the next level?", title="Please confirm")
if answer == True:
    easygui.msgbox(msg="Beginning level 17…")
else:
    easygui.msgbox(msg="Cancelling…")

answer = easygui.ynbox(msg="Go to the next level?", title="Please confirm")



   # custom button text with buttonbox:
directions = "Select a level"
levels = ["1", "2", "3", "4", "Quit"]
reply = easygui.buttonbox(msg=directions, choices=levels)



   # reply will have which button the user selected
if reply == "Quit":
    easygui.msgbox(msg="goodbye")
else:
    easygui.msgbox(msg= "You selected level " + reply)

'''
MANY MORE - ADVANCED FEATURES:
http://easygui.sourceforge.net/api.html
http://easygui.sourceforge.net/tutorial.html


ASSIGNMENT:
Write code to converse with the user about something, using easygui popup windows.
Also, go to the websites above and try to include one easygui feature that I did not
give you an example for above.
'''