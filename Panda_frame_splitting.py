import pandas as pd
def Splitting_and_concatination_of_CSV_Columns_single_tuple_first(df):    
        user_defined_dict_sensed_data_attributes_inCSV = {0: "id", 1: "fecha", 2: "tipo_elem", 3: "intensidad",
                                                          4: "ocupacion", 5: "carga", 6: "vmed", 7: "error",
                                                          8: "periodo_integracion"}
        splitted_column_data_frame = df['id;"fecha";"tipo_elem";"intensidad";"ocupacion";"carga";"vmed";"error";"periodo_integracion"'].str.split(";", expand=True).rename(user_defined_dict_sensed_data_attributes_inCSV, axis=1)
        splitted_column_data_frame = splitted_column_data_frame.apply(lambda x: x.str.strip('"'))         
        return splitted_column_data_frame 

