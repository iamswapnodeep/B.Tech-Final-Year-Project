import pandas as pd

# loading the path variables of the battery soh data>>
path_battery5 = "D:/College/Projects/Battery Status Monitoring/data/training_datasets/Training_Data_for_battery_5.csv"
path_battery6 = "D:/College/Projects/Battery Status Monitoring/data/training_datasets/Training_Data_for_battery_6.csv"
path_battery45 = "D:/College/Projects/Battery Status Monitoring/data/training_datasets/Training_Data_Battery-45.csv"
path_battery46 = "D:/College/Projects/Battery Status Monitoring/data/training_datasets/Training_Data_Battery-46.csv"
path_battery47 = "D:/College/Projects/Battery Status Monitoring/data/training_datasets/Training_Data_Battery-47.csv"
path_battery48 = "D:/College/Projects/Battery Status Monitoring/data/training_datasets/Training_Data_Battery-48.csv"

#setting up the SOH data
df = pd.read_csv(path_battery5)
soh_data_battery5 = df["soh"] 
df = pd.read_csv(path_battery6)
soh_data_battery6 = df["soh"]
df = pd.read_csv(path_battery45)
soh_data_battery45 = df["soh"] 
df = pd.read_csv(path_battery46)
soh_data_battery46 = df["soh"] 
df = pd.read_csv(path_battery47)
soh_data_battery47 = df["soh"] 
df = pd.read_csv(path_battery48)
soh_data_battery48 = df["soh"]

#check the soh data
print(soh_data_battery5) 
print(soh_data_battery6) 
print(soh_data_battery45) 
print(soh_data_battery46) 
print(soh_data_battery47) 
print(soh_data_battery48) 