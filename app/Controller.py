""" This module is in charge of executing commands from each script"""
# import ArucoModel as Ar
import PlantModel as PM
import View
import tkinter as tk
import threading
import time

# ================ View Script Setup ================= # 

root = tk.Tk() # Create the toplevel parent window
root.title('Plant Health Tracker')
# root.geometry('{}x{}'.format(1000, 600))

# Go through each row and column of parent window and configure
# Resize weight and minimum sizes
for i in range(4):
    root.columnconfigure(i, weight=1, minsize= 300)
for i in range(2):
    root.columnconfigure(i, weight=1, minsize=300)

myapp = View.View(root)

# ================= Model Script Setup ============== #
myPlantModel = PM.PlantModel(1,2,[0,0,0],[0,0,0],[0,0,0],[0,0,0],True,False)

# ================= Threading Setup ================= #
def model_thread():
    """ Thread to handle Model Script Execution """
    while(1):
        """ System Logic"""
        time.sleep(1) # Sleep to save resources
        print("Thread loop")
        if(myapp.button_pressed_flag==True):
            """ Update Data from View"""
            print("THREAD: Button Preassed")

            myPlantModel.is_database_updated=False
            while(myPlantModel.is_database_updated==False):
                print("THREAD: MODEL SCRIPT")
                myPlantModel.Update_DateBase()
                time.sleep(0.2) # Sleep to save resources
            print("THREAD: Data Updated")

            if(myPlantModel.is_database_updated==True):
                """ Command View to update """
                myapp.Update_From_JSON()
                myapp.Update_Photo_View()

                myapp.button_pressed_flag=False # reset flag

# ================= Execute Threads ================ #

thread_setup = threading.Thread(target=model_thread)
thread_setup.start()

myapp.mainloop()    

print("TEST")

