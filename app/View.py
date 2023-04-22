"""
This module is in charge of generating tkinter gui
"""
import tkinter as tk

class View(tk.Frame):
    """ View Module Class """
    plant_height = ""
    flower_to_leaf_ratio = 0.0
    green_to_green_max_ratio = 0.0



    def __init__(self, master):
        window = tk.Tk()\
        


    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

root = tk.Tk()
myapp = View(root)
myapp.print_contents(event=tk.)
myapp.mainloop() 