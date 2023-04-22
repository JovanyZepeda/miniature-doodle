"""
This module is in charge of generating tkinter gui
"""
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

class View(tk.Frame):
    """ View Module Class """



    def __init__(self, parent):
        tk.Frame.__init__(self,parent)
        self.parent = parent # Parent Frame Object pass when constructor is used
        #========== GUI Program ==========#
    
        plant_height = 0
        flower_to_leaf_ratio = 0.0
        green_to_green_max_ratio = 0.0

        test_str = "TEST"
        # Define a sytle object that is applied globally
        GUI_Style = ttk.Style()

        #Create frames that hold widgets
        frame_1 = tk.Frame(master=parent, width= 500, height=300, background="blue", relief="raised", borderwidth=1)
        frame_2 = tk.Frame(master=parent, width= 1000, height=300, background="green", relief="raised", borderwidth=1)
        frame_3 = tk.Frame(master=parent, width= 500, height= 300,background="red", relief="raised", borderwidth=1)

        
        # Create widgets for the UI
        button_1 = ttk.Button(master=frame_1, text=test_str, width=50)
        label_1 = ttk.Label(master=frame_1, text=test_str, width=50)
        label_2 = ttk.Label(master=frame_1, text=test_str, width=50)
        label_3 = ttk.Label(master=frame_1, text=test_str, width=50)
        label_4 = ttk.Label(master=frame_1, text=test_str, width=50)
        bar_1 = ttk.Progressbar(master=frame_1, orient="horizontal", length=50,mode="determinate", maximum=1, value=green_to_green_max_ratio )
        bar_2 = ttk.Progressbar(master=frame_1, orient="horizontal", length=50,mode="determinate", maximum=1, value=green_to_green_max_ratio )

        # Create widgets for photo view
        photo_view_1 = ttk.Label(master=frame_3,text=test_str, width=50 ,padding=3)
        photo_view_2 = ttk.Label(master=frame_2, text=test_str, width=50, padding=3)
        photo_view_3 = ttk.Label(master=frame_2,text=test_str, width=50, padding=3)

        # ========== Frame Layout ============#
        # GRID of parent = 3 rows and 2 columns
        # the parent is automatically split into a grid
        frame_1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        frame_3.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        frame_2.grid(row=1,columnspan=2, padx=5, pady=5, sticky="nsew")
        
        # =========== Widget Layout =============#
        # layout the widgets in frame_1 (Button Interface)
        button_1.grid(row=0)
        label_1.grid(row=1)
        label_2.grid(row=2)
        label_3.grid(row=3,column=0)
        label_4.grid(row=4,column=0)
        bar_1.grid(row=3, column=1)
        bar_2.grid(row=4, column=1)

        # Layout widgets in frame_3 (photo view 1)
        photo_view_1.pack()

        # Layout widget in frame 2 (photo view 2 and 3)
        photo_view_3.grid(row=0, column=0)
        photo_view_2.grid(row=0, column=1)
        

if __name__ == "__main__":
    root = tk.Tk() # Create the toplevel parent window
    root.title('Plant Health Tracker')
    root.geometry('{}x{}'.format(1000, 600))
    
    myapp = View(root)
    myapp.mainloop() 