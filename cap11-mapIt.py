#! /usr/bin/python3

import webbrowser as wb, sys, pyperclip as pc
if len(sys.argv) > 1:
    address = '+'.join(sys.argv[1:])
else:
    address = pc.paste()
wb.open('https://www.google.com/maps/place/'+address)
