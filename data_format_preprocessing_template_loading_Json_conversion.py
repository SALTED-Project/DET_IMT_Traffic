import pandas as pd
import os


number_of_sensor_processed = 0 # A variable to simply check the number of sensor processed and their data has been dumped into Json format

def  data_format_preprocessing_template_loading_Json_conversion( each_sensor_based_DF, traffic_flow_dict_template, single_sensor_dict_Composed_in_list, d_c_c):    
                
        for default_index, rows in each_sensor_based_DF.iterrows():            
            my_datetime = pd.Timestamp(each_sensor_based_DF.loc[default_index]["fecha"])          
                     
            
            my_datetime_str = my_datetime.strftime('%Y-%m-%dT%H:%M:%SZ')  # ISO 8601 datetime format
            startingTime = pd.to_datetime(my_datetime_str) - pd.Timedelta(minutes=15)
            traffic_flow_dict_template["id"] = "urn:ngsi-ld:TrafficFlowObserved:" + each_sensor_based_DF.loc[default_index]["id"] + ":" + my_datetime_str
            #print ("\n traffic_flow_dict_template", traffic_flow_dict_template["id"])
            
            traffic_flow_dict_template["dateObserved"] = {"type": "Property", "value": str(
                startingTime.strftime('%Y-%m-%dT%H:%M:%SZ')) + "/" + str(my_datetime_str)}
            traffic_flow_dict_template["dateObservedFrom"] = {"type": "Property", "value": {"@type": "DateTime",
                                                                                            "@value": startingTime.strftime(
                                                                                                '%Y-%m-%dT%H:%M:%SZ')}}
            traffic_flow_dict_template["dateObservedTo"] = {"type": "Property",
                                                            "value": {"@type": "DateTime", "@value": my_datetime_str}}

            traffic_flow_dict_template["dataprovider"] = {"type": "Property", "value": "https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=33cb30c367e78410VgnVCM1000000b205a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default"}
             if not pd.isna(each_sensor_based_DF.loc[default_index]["ocupacion"]): 
              
               traffic_flow_dict_template["Occupancy"] = {"type": "Property", "value": int (each_sensor_based_DF.loc[default_index]["ocupacion"] )}
            else : 
               traffic_flow_dict_template["Occupancy"] = {"type": "Property", "value": each_sensor_based_DF.loc[default_index]["ocupacion"] }
               
            if not pd.isna(each_sensor_based_DF.loc[default_index]["vmed"]):
              traffic_flow_dict_template["averageVehicleSpeed"] = {"type": "Property", "value": int ( each_sensor_based_DF.loc[default_index]["vmed"] )}
            else: 
              traffic_flow_dict_template["averageVehicleSpeed"] = {"type": "Property", "value":  each_sensor_based_DF.loc[default_index]["vmed"] }
             
	    traffic_flow_dict_template["intensity"] = {"type": "Property", "value": int (each_sensor_based_DF.loc[default_index]["intensidad"])}
            
            traffic_flow_dict_template["address"] = {"type": "Property", "value":
                each_sensor_based_DF.loc[default_index]["nombre"]}
            #********************************************************************************************************
            traffic_flow_dict_template["Location"] = {"type": "GeoProperty", "value": {"type": "LineString",
                                                                                       "coordinates": [str(
                                                                                           each_sensor_based_DF.loc[default_index][
                                                                                               "longitud"]),
                                                                                                       str(
                                                                                                           each_sensor_based_DF.loc[default_index][
                                                                                                               "latitud"])
                                                                                                       ]}}
            #********************************************************************************************************
            traffic_flow_dict_template["@context"] = list()
            traffic_flow_dict_template["@context"].append(
                each_sensor_based_DF.loc[default_index]["@context_0"])
            traffic_flow_dict_template["@context"].append(
               each_sensor_based_DF.loc[default_index]["@context_1"])
            traffic_flow_dict_template["type"] = \
            each_sensor_based_DF.loc[default_index]["type"]              
                                    
            if each_sensor_based_DF.loc[default_index]['id'] not in single_sensor_dict_Composed_in_list:
                single_sensor_dict_Composed_in_list[each_sensor_based_DF.loc[default_index]['id']] = []
                print ("\n\n\n*>>sensor is ",each_sensor_based_DF.loc[default_index]['id'] )
                         
            elif  each_sensor_based_DF.loc[default_index]['id'] in single_sensor_dict_Composed_in_list:
                single_sensor_dict_Composed_in_list[each_sensor_based_DF.loc[default_index]['id']].append (traffic_flow_dict_template)               
                traffic_flow_dict_template= {}

        # better to put here the folder name with year and month identification like "NGSILD_formatted_sensor_data_04_2019"
        folder_path = "User_Defined_output_dir"
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path,  f" Sensor "+list(single_sensor_dict_Composed_in_list.keys())[-1]+folder_path+".json")
        d_c_c= d_c_c + 1  #dictionary creating counter 
       
        if   file_path: 
                global number_of_sensor_processed
                number_of_sensor_processed = number_of_sensor_processed + 1
                print ("\n\n Generated Sensor file quantity", number_of_sensor_processed)
        
        file = open(file_path, "w")       
        for sens_lst in single_sensor_dict_Composed_in_list.values():          
                     
            for dict_of_sens_lst in sens_lst:                
                json_object = json.dumps(dict_of_sens_lst,  indent=4)#, separators=(",") )
                file.write(json_object)
                file.write(",")                    
            
        file.close()
        single_sensor_dict_Composed_in_list= {}
        
        #time.sleep (1)
	        

