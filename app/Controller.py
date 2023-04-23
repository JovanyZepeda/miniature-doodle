""" This module is in charge of executing commands from each script"""
# import ArucoModel as Ar
import PlantModel as PM
import View
import tkinter as tk
import threading
import time

# ================ View Script Setup ================= # 
G_VIEW_CLOSED_FLAG = False

root = tk.Tk() # Create the toplevel parent window
root.title('Plant Health Tracker')

# Go through each row and column of parent window and configure
# Resize weight and minimum sizes
for i in range(3):
    root.columnconfigure(i, weight=1, minsize= 300)
for i in range(2):
    root.columnconfigure(i, weight=1, minsize=300)

def on_quit():
    """Call this function when window is closed"""
    print("View window has been closed")
    global G_VIEW_CLOSED_FLAG
    root.destroy()
    G_VIEW_CLOSED_FLAG = True
    

root.protocol("WM_DELETE_WINDOW", on_quit)

myapp = View.View(root)

# ================= Model Script Setup ============== #
myPlantModel = PM.PlantModel(1,2,[0,0,0],[0,0,0],[0,0,0],[0,0,0],True,False)

# ================= Threading Setup ================= #
def model_thread():
    """ Thread to handle Model Script Execution """
    while(myapp.winfo_exists()):
        """ System Logic"""
        time.sleep(1) # Sleep to save resources
        print("Thread loop")
        if(myapp.button_pressed_flag==True):
            """ Update Data from View"""
            print("THREAD: Button Pressed")
            myapp.can_update_photo_view=False # prevent myApp from accessing database
            myPlantModel.is_database_updated=False

            while(myPlantModel.is_database_updated==False):
                print("THREAD: MODEL SCRIPT")
                myPlantModel.Update_DateBase()
                time.sleep(0.2) # Sleep to save resources
            print("THREAD: Data Updated")

            if(myPlantModel.is_database_updated==True):
                """ Command View to update """
                print("THREAD: Update from JSON and Update PhotoView")
                myapp.Update_From_JSON()

                myapp.button_pressed_flag=False # reset flag
                myapp.can_update_photo_view=True # Allow view script access to database
        
        # Check if the myApp View object still exists
        if G_VIEW_CLOSED_FLAG == True:
            break
# ================= Execute Threads ================ #

thread_setup = threading.Thread(target=model_thread)
thread_setup.start()

myapp.after(ms=5000, func=myapp.Update_Photo_View)

myapp.mainloop()    
print("END")

