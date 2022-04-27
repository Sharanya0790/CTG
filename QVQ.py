import numpy as np
import pandas as pd

#importing rawdata file
df = pd.read_csv("D:\\Python_check\\QVQ\\Rawdata.csv")

#summary
#Column headers
Header = list(df.columns.values)

#Actual No of packets received
Act_No_of_packets = len(df)

#Determine no of packets
#Condition to check packet reseting

min_seq_id = df["packet_sequence_id"].iloc[0]
max_seq_id = df["packet_sequence_id"].iloc[Act_No_of_packets-1]
print("min and max seq id",min_seq_id,max_seq_id)
if (max(df["packet_sequence_id"] == 65535)):
    packet_reset_st = 1
    max_seq_id_1 = 65535
    indexval = (df[df["packet_sequence_id"]== 65535].index.values)+1
    print("index val",indexval)
    No_of_packets_1 = max_seq_id_1 - min_seq_id
    print("No_of_packets_1",No_of_packets_1)
    min_seq_id_2 = df["packet_sequence_id"][indexval]
    print("min_seq_id_2",int(min_seq_id_2))
    No_of_packets_2 = max_seq_id - int(min_seq_id_2)
    print("No_of_packets_2",No_of_packets_2)
    Tot_no_of_packets = No_of_packets_1 + No_of_packets_2
    print("Tot_no_of_packets",(Tot_no_of_packets))
    
else:   
    Tot_no_of_packets = max_seq_id - min_seq_id
    print("Tot_no_of_packets",(Tot_no_of_packets))

#No of V packets

A_packets = df[df["packet_status"]== "A"]
A_packet_count = len(A_packets)
V_packet_count = Act_No_of_packets - A_packet_count
print("A and V packet count",A_packet_count,V_packet_count )
    
#Filtering ignition ON data

df1 = df[df["ignition_status"]== 1]

vehicle_odo = df1["vehicle_odometer"]
vehicle_dist = df1["vehicle_distance"]
fuel_consum = df1["fuel_consumption"]
engine_hrs = df1["engine_hours"]

header1= list(df1.columns.values)
vehicle_odo_idx = header1.index("vehicle_odometer")
df1.insert(vehicle_odo_idx,"vehicle_odo",vehicle_odo)
vehicle_dist_idx = header1.index("vehicle_distance")
df1.insert(vehicle_dist_idx,"vehicle_dist",vehicle_dist)
fuel_consumption_idx = header1.index("fuel_consumption")
df1.insert(fuel_consumption_idx,"fuel_consum",fuel_consum)
engine_hours_idx = header1.index("engine_hours")
df1.insert(engine_hours_idx,"engine_hrs",engine_hrs)

i=1
vehicle_odo_zero = 0
vehicle_dist_zero = 0
fuel_consum_zero = 0
engine_hrs_zero = 0

for i in range(1,len(df1)):
    if (df1["vehicle_odo"].iloc[i]== 0):
        df1["vehicle_odo"].iloc[i] = df1["vehicle_odo"].iloc[i-1]
        vehicle_odo_zero = vehicle_odo_zero + 1
        
    if (df1["vehicle_dist"].iloc[i]== 0):
        df1["vehicle_dist"].iloc[i] = df1["vehicle_dist"].iloc[i-1]
        vehicle_dist_zero = vehicle_dist_zero + 1
        
    if (df1["fuel_consum"].iloc[i]== 0):
        df1["fuel_consum"].iloc[i] = df1["fuel_consum"].iloc[i-1]
        fuel_consum_zero = fuel_consum_zero + 1
        
    if (df1["engine_hrs"].iloc[i]== 0):
        df1["engine_hrs"].iloc[i] = df1["engine_hrs"].iloc[i-1]
        engine_hrs_zero = engine_hrs_zero+1

print("vehicle odo zero count", vehicle_odo_zero)
print("vehicle dist zero count", vehicle_dist_zero)
print("Fuel consumption zero count", fuel_consum_zero)
print("Engine hours zero count", engine_hrs_zero)


writer = pd.ExcelWriter("D:\\Python_check\\QVQ\\Output.xlsx",engine = 'xlsxwriter')
df1.to_excel(writer,sheet_name='Data')
writer.save()
writer.close()



    