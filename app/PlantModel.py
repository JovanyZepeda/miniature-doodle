import cv2 as cv
import numpy as np
import sys 

#RGB/HSV Plot imports 
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

    def ColorSpace(): #This functions plots the RGB color space of the image in view_1_photos
        img = cv.imread("app\data\\view_1_photos\Picture.png")
        rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        hsv_img = cv.cvtColor(rgb_img, cv.COLOR_RGB2HSV)     

        #RGB Color Space
        r,g,b = cv.split(rgb_img)
        fig1 = plt.figure()
        axis1 = fig1.add_subplot(1, 1, 1, projection="3d")

        pixel_colors = rgb_img.reshape((np.shape(rgb_img)[0]*np.shape(rgb_img)[1], 3))
        norm = colors.Normalize(vmin=-1.,vmax=1.)
        norm.autoscale(pixel_colors)
        pixel_colors = norm(pixel_colors).tolist()

        axis1.scatter(r.flatten(), g.flatten(), b.flatten(), facecolors=pixel_colors, marker=".")
        axis1.set_xlabel("Red")
        axis1.set_ylabel("Green")
        axis1.set_zlabel("Blue")
        fig1.savefig("app\data\\view_4_photos\ColorSpace_RGB.png")

        #HSV Color Space 
        h, s, v = cv.split(hsv_img)
        fig2 = plt.figure()
        axis2 = fig2.add_subplot(1, 1, 1, projection="3d")

        pixel_colors = hsv_img.reshape((np.shape(hsv_img)[0]*np.shape(hsv_img)[1], 3))
        norm = colors.Normalize(vmin=-1.,vmax=1.)
        norm.autoscale(pixel_colors)
        pixel_colors = norm(pixel_colors).tolist()

        axis2.scatter(h.flatten(), s.flatten(), v.flatten(), facecolors=pixel_colors, marker=".")
        axis2.set_xlabel("Hue")
        axis2.set_ylabel("Saturation")
        axis2.set_zlabel("Value")
        fig2.savefig("app\data\\view_5_photos\ColorSpace_HSV.png")

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
    ColorSpace()
    #ColorSpace_HSV()


#myplant = PlantModel(1,2,3,4,True,False)

#print(myplant.does_plant_have_flowers)