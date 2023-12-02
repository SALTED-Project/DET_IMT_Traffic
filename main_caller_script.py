import pandas as pd
import os
import glob
import numpy as np
import threading
from threading import current_thread

#importing the user defined modules, availble within package

import Panda_frame_splitting
import sensor_information_file_processing
import merging_sensed_info_Plus_sensor_info
import context_adder_function
import groupBy_Splitting_the_merged_DF_func
import splitting_toget_groups
import data_series_interpolation

if __name__ == "__main__":
                
        Traffic_sensor_information = glob.glob(os.path.join("Sensor_information", "*.xlsx"))
        file_path = "04-2019.csv"   
        #Traffic_data_directory  = glob.glob(os.path.join("2019_sensed_data", "*.csv"))
	#if you have a directory of sensed data with mutiple csv files, use the above code line. Next, use the loop to get all files in directory, and enclose 
        #the below calls inside the iteration scope

        df = pd.read_csv ( file_path )
        # The below calls of functions follow the following format:
        # returned parameters = module name .function name

        splitted_column_data_frame_sensed_data = Panda_frame_splitting. Splitting_and_concatination_of_CSV_Columns_single_tuple_first(df)        
        splitted_sensor_info_DF= sensor_information_file_processing.sensor_information_file_processing(Traffic_sensor_information)                
        sensed_Plus_Sensor_info_merged_DF = merging_sensed_info_Plus_sensor_info. merging_sensed_info_Plus_sensor_info (splitted_column_data_frame_sensed_data, splitted_sensor_info_DF)                     
        sensed_Plus_Sensor_info_merged_DF = context_adder_function.context_adder_function( sensed_Plus_Sensor_info_merged_DF)
        grouped_by_sensed_Plus_Sensor_info_merged_DF  =  groupBy_Splitting_the_merged_DF_func. groupBy_Splitting_the_merged_DF_func (sensed_Plus_Sensor_info_merged_DF)         listOf_splitted_the_merged_sensed_data__Sensor_information_DF = splitting_toget_groups. splitting_toget_groups ( grouped_by_sensed_Plus_Sensor_info_merged_DF )
        data_series_interpolation.data_series_interpolation(listOf_splitted_the_merged_sensed_data__Sensor_information_DF)
        
        
        
        
