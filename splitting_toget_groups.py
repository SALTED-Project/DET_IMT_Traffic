import pandas as pd
import numpy as np
def splitting_toget_groups(grouped_by_sensed_Plus_Sensor_info_merged_DF ):
    listOf_splitted_the_merged_sensed_data__Sensor_information_DF = [grouped_by_sensed_Plus_Sensor_info_merged_DF.get_group(x) for x in grouped_by_sensed_Plus_Sensor_info_merged_DF.groups]
    print ("\nnumber of sensor  splitted into seprate dataFrames", len(listOf_splitted_the_merged_sensed_data__Sensor_information_DF))
    return listOf_splitted_the_merged_sensed_data__Sensor_information_DF

