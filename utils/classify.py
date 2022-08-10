
    ##############################################
    # 根据总分，利用K-means聚成3类                   #
    # 黑卡，金卡，银卡                              #
    # 分别显示每个类别的前3个球员                     #
    #                                            #
    #                                            #
    ##############################################


# from player.models import Pre_Player
import numpy as np
import pandas as pd

def load_data():
    csv_data = pd.read_csv("/home/wickked/django_football/player/lib/data.csv" , header=None )

    return csv_data

def dist(arrA , arrB):
    # print("A:",arrA)
    # print("B:" , arrB)
    dist = arrA - arrB
    dist = np.power(dist,2)
    # dist = np.sum(np.power(x,2),axis=1)
    return dist


def randCent(D , k):
    # n = D.shape[1]
    # D_min = D.iloc[ : , 1].min()
    # D_max = D.iloc[ : , 1].max()
    centers = np.array([66.787,80.662,90.853])
    centers = centers.reshape(-1,1)
    # centers = np.random.uniform(int(D_min) , int(D_max) , (k,1))
    return centers

def math_center(data):
    m,n = data.shape
    sum = [0,0,0]
    num = [0,0,0]
    for i in range(m):
        if(data.iloc[i,3] == 0):
            sum[0] += int(data.iloc[i,1])
            num[0] += 1
        elif(data.iloc[i,3] == 1):
            sum[1] += int(data.iloc[i,1])
            num[1] += 1
        elif(data.iloc[i,3] == 2):
            sum[2] += int(data.iloc[i,1])
            num[2] += 1
    for i in range(2):
        sum[i] /= num[i]
    center = np.array(sum)
    center = center.reshape(-1,1)
    return center

def Kmeans(D , k):
    m,n = D.shape
    centerx = randCent(D , k)
    center = centerx
    res_mid = np.zeros((m , 3))
    res_mid[: , 0] = np.inf
    res_mid[: , 1:3] = -1
    resultlist = pd.concat([D , pd.DataFrame(res_mid)] , axis = 1 , ignore_index = True)
    changed = True
    while changed:
        changed = False
        for i in range(m):
            dist1 = dist(int(D.iloc[i , 1]), center)
            resultlist.iloc[i , n] = dist1.min()
            resultlist.iloc[i , n + 1] = np.where(dist1 == dist1.min())[0]
            # print(resultlist)
        changed = not (resultlist.iloc[:, n + 1] == resultlist.iloc[ : , n + 2]).all()
        if changed:
            # cent_df = resultlist.groupby(n+1).mean()
            center = math_center(resultlist)
            # center = cent_df.iloc[ : , 0].values

            resultlist.iloc[: , n+2] = resultlist.iloc[: , n+1]
    return center , resultlist




D = load_data()
#overall是第4列
#数据只用到overall，所以不用数据归一化
player_id = D.iloc[  : 10000 , 0]
player_overall = D.iloc[  : 10000 , 4]

data = pd.concat([player_id , player_overall] , axis = 1 , ignore_index = True)
data.index = range(len(data))

center , res = Kmeans(data , 3)
data = pd.concat([D , res.iloc[ : , 3]] , axis=1 , ignore_index=True)
data.sort_values([9],inplace=True)
data.sort_values([4],ascending=False,inplace=True)
players = data.groupby([9]).head(3)
print(players)
# for i in range(len(players)):
#     player = players.iloc[i]
#     player = Pre_Player(id=player.player_id, player_name=player.player_name, nationality=player.nationality,
#                     position=player.position,
#                     overall=player.overall, age=player.age, hits=player.hits, potential=player.potential,
#                     team=player.team)
#     player.save()
# print(center , res)
#data.columns = ['id', 'overall', 'dist', 'class', 'preclass']
# resultlist = pd.concat([D , pd.DataFrame(res_mid)] , axis = 1 , ignore_index = True)