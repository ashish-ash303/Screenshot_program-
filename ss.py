import pyautogui
# import tkinter as tk

from tkinter.filedialog import *

# root = tk.Tk()
# window = tk.Canvas(root, width=300, height=300)
# window.pack()

input = input("Press S key to Take your Screenshot")


def ss_take():

    screen_shot = pyautogui.screenshot()
    save_path = asksaveasfilename()
    screen_shot.save(save_path + "_screenshot.png")


if(input == " S"):
    ss_take()

else:
    print("Error")


# ss_button = tk.Button(text="TAKE  YOUR SCREENSHOT ",
#                       command=ss_take, font=20)

# window.create_window(150, 150, window=ss_button)

# # time.sleep(4)
# root.mainloop()
