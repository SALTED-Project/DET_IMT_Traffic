import pandas as pd
import glob
import numpy as np
def merging_sensed_info_Plus_sensor_info (splitted_column_data_frame_sensed_data, splitted_sensor_info_DF): 
    
    sensed_Plus_Sensor_info_merged_DF = pd.merge(splitted_column_data_frame_sensed_data, splitted_sensor_info_DF,left_on='id', right_on='id', how='left')
    print("\n sensed_Plus_Sensor_info_merged_DF.head (5)", sensed_Plus_Sensor_info_merged_DF.head (5))
    #print ("\n\n unique ids in merged matrics", len(pd.unique(sensed_Plus_Sensor_info_merged_DF["id"]  )))
    return sensed_Plus_Sensor_info_merged_DF
