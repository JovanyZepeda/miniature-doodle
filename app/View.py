"""
This module is in charge of generating tkinter gui
"""
import tkinter as tk
from tkinter import ttk

class View(tk.Frame):
    """ View Module Class """



    def __init__(self, parent):
        tk.Frame.__init__(self,parent)
        self.parent = parent # Parent Frame Object pass when constructor is used
        #========== GUI Program ==========#
    
        plant_height = ""
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
        button_1 = ttk.Button(master=frame_1, text=test_str)
        label_1 = ttk.Label(master=frame_1, text=test_str)
        label_2 = ttk.Label(master=frame_1, text=test_str)
        label_3 = ttk.Label(master=frame_1, text=test_str)
        label_4 = ttk.Label(master=frame_1, text=test_str)

        # Create widgets for photo view
        photo_view_1 = ttk.Label(master=frame_3,text=test_str)
        photo_view_2 = ttk.Label(master=frame_2, text=test_str)
        photo_view_3 = ttk.Label(master=frame_2,text=test_str)

        # ========== Frame Layout ============#
        # GRID of parent = 3 rows and 2 columns
        # the parent is automatically split into a grid
        frame_1.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        frame_3.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        frame_2.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        
        # =========== Widget Layout =============#


if __name__ == "__main__":
    root = tk.Tk() # Create the toplevel parent window
    root.title('Plant Health Tracker')
    root.geometry('{}x{}'.format(1000, 600))
    # root.rowconfigure([0, 1, 2])
    # root.columnconfigure([0,2])
    myapp = View(root)
    myapp.mainloop() 