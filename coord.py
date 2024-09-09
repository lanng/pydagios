import pyautogui
import keyboard
import time

# script to mesure the pixels coord. to put on main.py

stop=0

while True:
    start=time.time()
    #Get the coordinates of mouse pointer or cursor everytime 'z' key is pressed
    if keyboard.is_pressed('a') and (start-stop)>1:
        # Get the X and Y coordinates of the mouse pointer or curser
        position = pyautogui.position()
        print(position)
        stop=time.time()