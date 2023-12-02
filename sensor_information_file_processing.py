
import pandas as pd
import os
import glob


def  sensor_information_file_processing(): 
    for sens_info in Traffic_sensor_information:
            #its in CSV SO NO NEED TO SPLIT IT
            print("\n sens_info", sens_info)
            
            sensed_info_DF = pd.read_excel(sens_info)
            sensed_info_DF['id'] = sensed_info_DF['id'].astype(str)#.str.lstrip('0')
            print("sensed_info_DF.column ",sensed_info_DF.columns)
            return sensed_info_DF
        
