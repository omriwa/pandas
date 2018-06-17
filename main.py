import pandas as pd
import numpy as np


def Total_tickets_per_week_and_movie(file_p):
    #reading the data from file
    df = pd.read_csv(file_p) 
    #grouping the data
    groups = df.groupby(['calendarweek','movie','auditorium_row'])
    #count the groups and print the output
    print groups.size()

def Seat_load_factor_per_week_and_movie(file_p1,file_p2):
    #reading the data from file
    df_sold = pd.read_csv(file_p1) 
    df_capacity = pd.read_csv(file_p2) 
    #creating merge df
    merge_df = pd.merge(df_sold,df_capacity,on='auditorium_row')
    #grouping the data
    groups = merge_df.groupby(['calendarweek','movie','auditorium_row'])
    output = []
    
    for group in groups:
        temp = group[1]
        temp[''] =  temp['movie'].size / float(temp['max_seats_per_row'].iloc[0]) 
        output.append(temp)
    
    return output
    
def Seat_load_factor_per_week_row(file_p1,file_p2):
    """
    could not make this function due the lack of time and data manipulation
    Seat_load_factor_per_week_and_movie func,
    group by week,
    sum the seat_load_factor that was calculated in Seat_load_factor_per_week_and_movie func and devide by the size of the group
    print in the desiered format
    """
    
"""
P.S

didnt have any exprience with pandas before, the logic is easy but the framework exprience played a big role with manipulation the data,
and form the desired output.

Best,

Omri
"""