import pandas as pd
import numpy as np
import os

def load_data():
    #读取整个CSV文件
    csv_data = pd.read_csv("../player/lib/FIFA-21 Complete.csv")

    return csv_data

def deal_data(data):
    df = pd.DataFrame(columns=('player_id','name','nationality','position','overall','age','hits','potential','team'))
    for i in range(0,17980):
        data_split = str(data.loc[i,'player_id']).split(';') #['158023', 'Lionel Messi', 'Argentina', 'ST|CF|RW', '94', '33', '299', '94', '"FC Barcelona "']
        player_id = int(data_split[0])
        name = data_split[1]
        nationality = data_split[2]
        position = data_split[3]
        overall = int(data_split[4])
        age = int(data_split[5])
        hits = int(data_split[6])
        potential = int(data_split[7])
        team = data_split[8]
        df = df.append(pd.DataFrame({'player_id':[player_id],
                                     'name':[name],
                                     'nationality':[nationality],
                                     'position':[position],
                                     'overall':[overall],
                                     'age':[age],
                                     'hits':[hits],
                                     'potential':[potential],
                                     'team':[team]}))
    df = df.dropna().reset_index(drop=True)

    return df


data = load_data()
df = deal_data(data)
df.to_csv("../player/lib/data.csv" , header=True , index=False)
#print(df)

#print(data.loc[0])
#print(data.loc[0 , 'player_id']) #158023;Lionel Messi;Argentina;ST|CF|RW;94;33;299;94;"FC Barcelona "