import pandas as pd
import os
import glob
import string
import sys
import threading
import numpy as np
import re
import time
import json
import time
from os import getpid
from os import getppid
from threading import current_thread
from concurrent.futures import ProcessPoolExecutor

import threading
from threading import current_thread



def  groupBy_Splitting_the_merged_DF_func (sensed_Plus_Sensor_info_merged_DF): 
    #print ("\n\n colums names in sensed_Plus_Sensor_info_merged_DF", sensed_Plus_Sensor_info_merged_DF.columns())
    grouped_by_sensed_Plus_Sensor_info_merged_DF =  sensed_Plus_Sensor_info_merged_DF.groupby("id") 
  
    print("\n\n\n\n len( grouped_by_sensed_Plus_Sensor_info_merged_DF)", len( grouped_by_sensed_Plus_Sensor_info_merged_DF))
    return grouped_by_sensed_Plus_Sensor_info_merged_DF

