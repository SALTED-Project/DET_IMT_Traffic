
import pandas as pd
import os
import glob

def context_adder_function(sensed_Plus_Sensor_info_merged_DF):

    sensed_Plus_Sensor_info_merged_DF.insert(0, "type", "TrafficFlowObserved")    
    sensed_Plus_Sensor_info_merged_DF.insert(0, "@context_2","https://raw.githubusercontent.com/SALTED-Project/contexts/main/context.jsonld"  )
    sensed_Plus_Sensor_info_merged_DF.insert(0, "@context_1",
                                                  "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld")
    sensed_Plus_Sensor_info_merged_DF.insert(0, "@context_0",
                                                  "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld")
    print(sensed_Plus_Sensor_info_merged_DF.head(2))   
    
    return sensed_Plus_Sensor_info_merged_DF

