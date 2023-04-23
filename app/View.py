"""
This module is in charge of generating tkinter gui
"""
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
import os
import json

G_CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
G_PLANT_MODEL_FILE = os.path.join(G_CURRENT_DIR, "data", "plant_model_data.json")
G_ARUCO_MODEL_FILE = os.path.join(G_CURRENT_DIR, "data", "plant_height_data.json")
G_VIEW_PHOTO_DIR   = os.path.join(G_CURRENT_DIR, "data", "view_photos")

class View(tk.Frame):
    """ View Module Class """

    def __init__(self, parent):
        tk.Frame.__init__(self,parent)
        self.parent = parent # Parent Frame Object pass when constructor is used
        
        #========== GUI Program ==========#
    
        self.Update_From_JSON()

        self.button_pressed_flag = False
        self.can_update_photo_view = False

        # =============== Photo Access ============#
        current_path = os.path.dirname(__file__)
        self.photo_vew_1_dir = os.path.join(G_VIEW_PHOTO_DIR, "Picture.png" )
        self.photo_vew_2_dir = os.path.join(G_VIEW_PHOTO_DIR, "ColorSpace_RGB.png")
        self.photo_vew_3_dir = os.path.join(G_VIEW_PHOTO_DIR, "ColorSpace_HSV.png")
        self.photo_vew_4_dir = os.path.join(G_VIEW_PHOTO_DIR,  "Flowers.png")
        self.photo_vew_5_dir = os.path.join(G_VIEW_PHOTO_DIR,  "Leaves.png")
        self.photo_vew_6_dir = os.path.join(G_VIEW_PHOTO_DIR, "Flowers.png")
        self.photo_vew_7_dir = os.path.join(G_VIEW_PHOTO_DIR,  "Flowers.png")
        
        # Store a reference to th image
        self.img_1 = ImageTk.PhotoImage(Image.open(self.photo_vew_1_dir).resize((300,225)))
        self.img_2 = ImageTk.PhotoImage(Image.open(self.photo_vew_2_dir).resize((300,225)))
        self.img_3 = ImageTk.PhotoImage(Image.open(self.photo_vew_3_dir).resize((300,225)))
        self.img_4 = ImageTk.PhotoImage(Image.open(self.photo_vew_4_dir).resize((300,225)))
        self.img_5 = ImageTk.PhotoImage(Image.open(self.photo_vew_5_dir).resize((300,225)))
        self.img_6 = ImageTk.PhotoImage(Image.open(self.photo_vew_6_dir).resize((300,225)))
        self.img_7 = ImageTk.PhotoImage(Image.open(self.photo_vew_7_dir).resize((300,225)))

        test_str = "TEST"
        # Define a sytle object that is applied globally
        GUI_Style = ttk.Style()

        #Create frames that hold widgets
        frame_2 = tk.Frame(master= parent, width= 310, height= 230, relief= "raised", borderwidth= 1)
        frame_3 = tk.Frame(master= parent, width= 310, height= 230, relief= "raised", borderwidth= 1)
        frame_1 = tk.Frame(master= parent, width= 310, height= 230, relief= "raised", borderwidth= 1)
        frame_4 = tk.Frame(master= parent, width= 310, height= 230, relief= "raised", borderwidth= 1)
        frame_5 = tk.Frame(master= parent, width= 310, height= 230, relief= "raised", borderwidth= 1)
        frame_6 = tk.Frame(master= parent, width= 310, height= 230, relief= "raised", borderwidth= 1)
        frame_7 = tk.Frame(master= parent, width= 310, height= 230, relief= "raised", borderwidth= 1)
        frame_8 = tk.Frame(master= parent, width= 310, height= 230, relief= "raised", borderwidth= 1)

    
        # Create widgets for the UI (Frame 1)
        button_1 = ttk.Button(master=frame_1, text="Take a Picture", command=self.Handle_button_1_press, width=15)
        label_1 = ttk.Label(master=frame_1, text="Plant Height (in): " + str(self.plant_height), width=25)
        label_2 = ttk.Label(master=frame_1, text="Flower to Leaf Ratio: " + str(self.flower_to_leaf_ratio), width=25)
        label_3 = ttk.Label(master=frame_1, text="Plant Health Bar:", width=20)
        label_4 = ttk.Label(master=frame_1, text="Flower level Bar: ", width=20)
        bar_1 = ttk.Progressbar(master=frame_1, orient="horizontal", length=100,mode="determinate", maximum=1, value=self.green_to_green_max_ratio )
        bar_2 = ttk.Progressbar(master=frame_1, orient="horizontal", length=100,mode="determinate", maximum=1, value=self.flower_to_leaf_ratio )
        self.bar_3 = ttk.Progressbar(master=frame_1, orient="horizontal", length=100,mode="indeterminate")

        # Create widgets for photo view
        self.photo_1_title = "Original Photo"
        self.photo_2_title = "RGB Scatter Plot"
        self.photo_3_title = "HSV Scatter Plot"
        self.photo_4_title = "Segmented Photo - Flower Only - Color"
        self.photo_5_title = "Segmented Photo - Flower Only - no Color"
        self.photo_6_title = "Segmented Photo - Leaves Only - Color"
        self.photo_7_title = "Segmented Photo - Leaves Only - No Color"

        self.photo_view_1 = ttk.Label(master=frame_2,image=self.img_1, text=self.photo_1_title, compound="bottom" , width=10 ,padding=3)
        self.photo_view_2 = ttk.Label(master=frame_6,image=self.img_2, text=self.photo_2_title, compound="bottom" , width=10, padding=3)
        self.photo_view_3 = ttk.Label(master=frame_5,image=self.img_3, text=self.photo_3_title, compound="bottom", width=10, padding=3)
        self.photo_view_4 = ttk.Label(master=frame_3,image=self.img_4, text=self.photo_4_title, compound="bottom" , width=10 ,padding=3)
        self.photo_view_5 = ttk.Label(master=frame_7,image=self.img_5, text=self.photo_5_title, compound="bottom" , width=10, padding=3)
        self.photo_view_6 = ttk.Label(master=frame_4,image=self.img_6, text=self.photo_6_title, compound="bottom", width=10, padding=3)
        self.photo_view_7 = ttk.Label(master=frame_8,image=self.img_7, text=self.photo_7_title, compound="bottom" , width=10 ,padding=3)

        # ========== Frame Layout ============#
        # GRID of parent = 3 rows and 2 columns
        # the parent is automatically split into a grid
        frame_1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        frame_2.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        frame_3.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
        # frame_4.grid(row=0, column=3, padx=5, pady=5, sticky="nsew")

        frame_5.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        frame_6.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        frame_7.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
        # frame_8.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")
        
        # =========== Widget Layout =============#
        # layout the widgets in frame_1 (Button Interface)
        button_1.grid(row=0, columnspan= 2, padx=5, pady=5, sticky="ew")
        label_1.grid(row=1, padx=5, pady=5, sticky="ew")
        label_2.grid(row=2, padx=5, pady=5, sticky="ew")
        label_3.grid(row=3,column=0, padx=5, pady=5, sticky="ew")
        label_4.grid(row=4,column=0, padx=5, pady=5, sticky="ew")
        bar_1.grid(row=3, column=1, padx=5, pady=5, sticky="e")
        bar_2.grid(row=4, column=1, padx=5, pady=5, sticky="e")
        self.bar_3.grid(row=5, columnspan= 2, padx=5, pady=5, sticky="ew")

        # Layout widgets in the photo frames (photo view 1)
        self.photo_view_1.pack()
        self.photo_view_2.pack()
        self.photo_view_3.pack()
        self.photo_view_4.pack()
        self.photo_view_5.pack()
        self.photo_view_6.pack()
        self.photo_view_7.pack()
        
    def Update_From_JSON(self):
        """Helper Function to extract JSON Data"""
        with open(G_PLANT_MODEL_FILE, "r") as json_file:

            plant_model_dict = json.load(json_file)
        
            self.flower_to_leaf_ratio = plant_model_dict["flower_to_leaf_ratio"]
            self.green_to_green_max_ratio = plant_model_dict["green_to_green_max_ratio"]
        
        with open(G_ARUCO_MODEL_FILE, "r") as json_file:
            aruco_model_dict = json.load(json_file)

            self.plant_height = aruco_model_dict["plant_height"]

    def Update_Photo_View(self):
        """Call this to update photo views"""
        print("Updating Photo View")

        if(self.can_update_photo_view==True):

            # Store a reference to th image 
            self.img_1 = ImageTk.PhotoImage(Image.open(self.photo_vew_1_dir).resize((300,225)))
            self.img_2 = ImageTk.PhotoImage(Image.open(self.photo_vew_2_dir).resize((300,225)))
            self.img_3 = ImageTk.PhotoImage(Image.open(self.photo_vew_3_dir).resize((300,225)))
            self.img_4 = ImageTk.PhotoImage(Image.open(self.photo_vew_4_dir).resize((300,225)))
            self.img_5 = ImageTk.PhotoImage(Image.open(self.photo_vew_5_dir).resize((300,225)))
            self.img_6 = ImageTk.PhotoImage(Image.open(self.photo_vew_6_dir).resize((300,225)))
            self.img_7 = ImageTk.PhotoImage(Image.open(self.photo_vew_7_dir).resize((300,225)))

            self.photo_view_1.configure(image=self.img_1)
            self.photo_view_2.configure(image=self.img_2)
            self.photo_view_3.configure(image=self.img_3)
            self.photo_view_4.configure(image=self.img_4)
            self.photo_view_5.configure(image=self.img_5)
            self.photo_view_6.configure(image=self.img_6)
            self.photo_view_7.configure(image=self.img_7)


            self.photo_view_1.update()
            self.photo_view_2.update()
            self.photo_view_3.update()
            self.photo_view_4.update()
            self.photo_view_5.update()
            self.photo_view_6.update()
            self.photo_view_7.update()

            self.bar_3.stop()

        self.after(ms=5000, func=self.Update_Photo_View)
    
    def Handle_button_1_press(self):
        """ Event handler when button 1 is pressed """
        self.button_pressed_flag = True
        self.bar_3.start()
        print("BUTTON PRESSED")

if __name__ == "__main__":
    root = tk.Tk() # Create the toplevel parent window
    root.title('Plant Health Tracker')
    # root.geometry('{}x{}'.format(1000, 600))

    # Go through each row and column of parent window and configure
    # Resize weight and minimum sizes
    for i in range(4):
        root.columnconfigure(i, weight=1, minsize= 300)
    for i in range(2):
        root.columnconfigure(i, weight=1, minsize=300)
    
    

    myapp = View(root)

    myapp.Update_From_JSON()

    myapp.mainloop() 


