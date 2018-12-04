#! python3

# mapit.py - launches map in browser from command line

#C:\Users\cudolan\Desktop\New folder\
#https://www.google.com/maps/place/1307+S+Wabash+Ave,+Chicago,+IL+60605/

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    #get the address in cmd line
    address = ' '.join(sys.argv[1:])
    #1: because the first element in the array is the file name
else:
    # Get address from clipboard.
    address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/' + address)

