# Traffic Data Enrichment Toolchain by IMT

## Introduction

#### 📝 Description
This Python scripts includes the functions for the conversion of traffic-sensed data. The data is collected from the Madrid city open portal. The under-consideration data is traffic observation for a month and each sensor collects the data after fifteen minutes. The scripts perform the data preprocessing (e.g., formatting, missing data interpolation, merging the sensor information with sensed data ) and convert it into an NGSI-LD format. This process utilizes the TrafficFlowObserved smart data model specification for enriching and context awareness of data.

#### :arrow_forward: Workflow
-   The main_caller_script read the input data and calls the different functions necessary to process the data .
-   A script (sensed_Plus_Sensor_info_merged_DF) merges the information of sensed data (i.e., traffic intensity, average speed) with corresponding sensor meta information (i.e., sensor ID, location, location coordinates).
-   The volume of monthly uploaded data in the source portal is large, so the merged information is further split into each sensor-based segregated data frame.
-   A template is developed using the components of the TrafficFowObserved data model and loaded the each single observation (data tuple) in the template. 
-   The template holds the traffic sensed data in the form of key, value that further dumped into JSON-LD format.

#### :sparkles: Other components
N/A

#### 📧 Contact
All code located in this repository was developed by [DICE Lab](https://dice.wp.telecom-sudparis.eu/) at [IMT](https://www.telecom-sudparis.eu/).

## Installation
### Prerequisites
To successfully execute the scripts make sure that the Python (3 or above version) is installed on your machine. You can install the required libraries using the following command:
pip install pandas 
pip install numpy

### Usage
Navigate to the main script and execute it. You have to provide the path of the directory or file in the main script, which has sensed data contents. 
python main_caller_script.py

### Batch Traffic Data Volume Conversion
If these scripts will be used for the processing and conversion of large CSV files, then follow the guide (comments) in code to enable the concurrent outstreaming in the files.

## Acknowledgment 
This work was supported by the European Commission CEF Programme by means of the project SALTED ‘‘Situation-Aware Linked heterogeneous Enriched Data’’ under the Action Number 2020-EU-IA-0274.

## License
 N/A



