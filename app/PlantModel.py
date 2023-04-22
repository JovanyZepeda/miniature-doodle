import sys 

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

    def TakePicture():
        

#myplant = PlantModel(1,2,3,4,True,False)

#print(myplant.does_plant_have_flowers)