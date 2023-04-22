import cv2 as cv
import numpy as np
import sys 

#RGB Plot imports 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors

class PlantModel:
    flower_to_leaf_ratio = 0.0
    green_to_green_max_ratio = 0.0
    green_color_minimum = 0.0
    green_color_maximum = 0.0
    does_plant_have_flowers = False 
    is_plant_healthy = False

    def __init__(self,flower_to_leaf_ratio, green_to_green_max_ratio,
                     green_color_minimum, green_color_maximum,
                     does_plant_have_flowers, is_plant_healthy):
        
        self.flower_to_leaf_ratio = flower_to_leaf_ratio
        self.green_to_green_max_ratio =  green_to_green_max_ratio
        self.green_color_minimum = green_color_minimum
        self.green_color_maximum = green_color_maximum
        self.does_plant_have_flowers = does_plant_have_flowers
        self.is_plant_healthy = is_plant_healthy

    def TakePicture(): #ThisFunction Take a Picture and stores the image in view_1_photos
        cam_port = 0
        cam = cv.VideoCapture(cam_port)
        result, img = cam.read()
        if result:
            cv.imshow("Display window", img)
            cv.imwrite("app\data\\view_1_photos\Picture.png", img)
            cv.waitKey(0)
        else:
            print("No Image Detected")

    def ColorSpace_RGB(): #This functions plots the RGB color space of the image in view_1_photos
        img = cv.imread("app\data\\view_1_photos\Picture.png")
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        r,g,b = cv.split(img)
        fig = plt.figure()
        axis = fig.add_subplot(1, 1, 1, projection="3d")

        pixel_colors = img.reshape((np.shape(img)[0]*np.shape(img)[1], 3))
        norm = colors.Normalize(vmin=-1.,vmax=1.)
        norm.autoscale(pixel_colors)
        pixel_colors = norm(pixel_colors).tolist()

        axis.scatter(r.flatten(), g.flatten(), b.flatten(), facecolors=pixel_colors, marker=".")
        axis.set_xlabel("Red")
        axis.set_ylabel("Green")
        axis.set_zlabel("Blue")
        plt.show()

    def ColorSpace_HSV():
        img = cv.imread("app\data\\view_1_photos\Picture.png")
        hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

        h, s, v = cv.split(hsv_img)
        fig = plt.figure()
        axis = fig.add_subplot(1, 1, 1, projection="3d")

        pixel_colors = img.reshape((np.shape(img)[0]*np.shape(img)[1], 3))
        norm = colors.Normalize(vmin=-1.,vmax=1.)
        norm.autoscale(pixel_colors)
        pixel_colors = norm(pixel_colors).tolist()

        axis.scatter(h.flatten(), s.flatten(), v.flatten(), facecolors=pixel_colors, marker=".")
        axis.set_xlabel("Hue")
        axis.set_ylabel("Saturation")
        axis.set_zlabel("Value")
        plt.show()

    def ID_Leaves(): #This function reads the image in view_1_photos and Identify the plants leaves 
        img = cv.imread("app\data\\view_1_photos\Picture.png")
        new_img = np.zeros(img.shape, img.dtype)

        cv.imshow('Original Image', img)
        cv.imshow('New Image', new_img)
        cv.imwrite("app\data\\view_2_photos\Leaves.png", img)
        cv.waitKey(0)

    def ID_Flowers(): #This function read the image in view_1_photos and Identify the plants flowers
        img = cv.imread("app\data\\view_1_photos\Picture.png")
        new_img = np.zeros(img.shape, img.dtype)

        cv.imshow('Original Image', img)
        cv.imshow('New Image', new_img)
        cv.imwrite("app\data\\view_3_photos\Flowers.png", img)
        cv.waitKey(0)
    
    TakePicture()
    ColorSpace_RGB()
    ColorSpace_HSV()


#myplant = PlantModel(1,2,3,4,True,False)

#print(myplant.does_plant_have_flowers)