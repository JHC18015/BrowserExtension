from tkinter import *
import tkinter as tk
import random
from win32api import GetSystemMetrics

root = tk.Tk()

screenWidth = GetSystemMetrics(0)
screenHeight = GetSystemMetrics(1)

x = root.winfo_x()
y = root.winfo_y()

moveHor = False
moveVert = False

print(screenWidth)
print(screenHeight)

def create_window():
    new_window = tk.Tk()
    screenWidth = GetSystemMetrics(0)
    screenHeight = GetSystemMetrics(1)
    new_window.geometry("100x100+{}+{}".format(screenWidth // 2, screenHeight // 2))
    new_window.after(200, stay_on_top)
    new_window.protocol("WM_DELETE_WINDOW", create_window)

def toe_pics():
    global screenWidth, screenHeight, x, y, moveHor, moveVert
    
    if (x > -1 and x < screenWidth and moveHor == False):
        x += 5
    else:
        x -= 5
        if (x > -1):
            moveHor = True
        else:
            moveHor = False
                
    if (y > -1 and y < screenHeight and moveVert == False):
        y += 5
    else:
        y -= 5
        moveVert = True
                
    if (y < -1):
        y += 10
        moveVert = False
            
    if (x < -1):
        x += 10
        moveHor = False
    
    root.geometry('%dx%d+%d+%d' % (100, 100, x, y))
    root.after(10, toe_pics)

def stay_on_top():
    root.wm_attributes("-topmost", True)
    root.after(20, stay_on_top)

root.after(20, toe_pics)
root.after(100, stay_on_top)
root.protocol("WM_DELETE_WINDOW", create_window)
root.mainloop()
