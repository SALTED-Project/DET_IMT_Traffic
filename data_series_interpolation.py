
import pandas as pd
import os
import numpy as np

import data_format_preprocessing_template_loading_Json_conversion

def data_series_interpolation (listOf_splitted_the_merged_sensed_data__Sensor_information_DF):    

    d_c_c = 0      
    for each_sensor_based_DF in listOf_splitted_the_merged_sensed_data__Sensor_information_DF: 
            traffic_flow_dict_template = dict()
            single_sensor_dict_Composed_in_list= {}
            thread_list= []
            each_sensor_based_DF = each_sensor_based_DF.applymap(lambda x: x.strip('"') if isinstance(x, str) else x)
            
            nan_indices = each_sensor_based_DF["ocupacion"][each_sensor_based_DF ["ocupacion"] == 'NaN'].index
            nan_indices_vmed = each_sensor_based_DF["vmed"][each_sensor_based_DF ["vmed"] == 'NaN'].index
                                  
            if (len (list(nan_indices_vmed)) != 0):
            		
            	each_sensor_based_DF["vmed"] = each_sensor_based_DF["vmed"].replace('NaN', np.nan)
            	each_sensor_based_DF["vmed"] = pd.to_numeric(each_sensor_based_DF["vmed"], errors='coerce')
            	each_sensor_based_DF["vmed"] = each_sensor_based_DF["vmed"].interpolate ()           
            
            if ( len (list(nan_indices)) != 0):              
              each_sensor_based_DF["ocupacion"] = each_sensor_based_DF["ocupacion"].replace('NaN', np.nan)
                           
              each_sensor_based_DF["intensidad"] = pd.to_numeric(each_sensor_based_DF["intensidad"], errors='coerce')
              
              each_sensor_based_DF["ocupacion"] = pd.to_numeric(each_sensor_based_DF["ocupacion"], errors='coerce')
              
              each_sensor_based_DF["ocupacion"] = each_sensor_based_DF["ocupacion"].interpolate ()              
              
              remaining_nan = each_sensor_based_DF['ocupacion'].isnull().sum()

            data_format_preprocessing_template_loading_Json_conversion.data_format_preprocessing_template_loading_Json_conversion(each_sensor_based_DF, traffic_flow_dict_template, single_sensor_dict_Composed_in_list,d_c_c )

            #Note: You can activate multithreading here if there are a lot of individual sensor files. Concurrent writing to the user-specified output directory will begin.

            """
            thread_list.append(  threading.Thread(target=data_format_preprocessing_template_loading_Json_conversion.data_format_preprocessing_template_loading_Json_conversion, args=(each_sensor_based_DF, traffic_flow_dict_template, single_sensor_dict_Composed_in_list,d_c_c )) )
            thread_list[-1].start()
            thread_list[-1].join()
            #you can introduce delay here
            """
            
        
            
