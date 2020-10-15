# Webbrowser exploration

import webbrowser

go = input("Ready?  Some windows are about to open...(hit enter) ")

# Open URL in a new tab, if a browser window is already open:
url = 'http://docs.python.org/'

webbrowser.open_new_tab(url)

# Open URL in new window, raising the window if possible:
webbrowser.open_new(url)

#open in specific browswer
brwsr = webbrowser.get('firefox')
brwsr.open('http://www.google.com')

brwsr2 = webbrowser.get('safari')
brwsr2.open('http://www.weather.com')

'''
ASSIGNMENT:
 1. Write code that would let the user type in a web address they want to go to and
   open that site
You should ask the user for a valid URL 

OPTIONAL: tell them they don't need "http://" and when they type in their address,
    you can add the http:// to it before opening that webpage

 2.  Ask the user for a number and use a for-loop open that many tabs with
      some website
'''
