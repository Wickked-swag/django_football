import json

from django.contrib.sessions import serializers
from django.core import serializers
from django.core.serializers import serialize
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from player.models import Player
from player.models import User
from player.models import User_team,User_player,Pre_Player
#######################################
#开发者日志                             #
#day1.大体思路是：后台数据处理写成函数形式  #
#在这里进行调用，最终结果以字典形式返回前端  #
#按钮绑定action,被usrl捕捉后传递到views中 #
#day2.to be continue                  #
#                                     #
#                                     #
#                                     #
#                                     #
#                                     #
#                                     #
#######################################

name = None
user_id = None
def index(request):
    return render(request , 'index.html')

def login(request):
    ##########################
    #数据库查询用户的账户密码     #
    #匹配账户密码              #
    #登陆成功后跳转到球员首页     #
    #登陆失败跳转index.html页面 #
    #done                    #
    ##########################
    flag = False
    global name,user_id
    name = request.POST['name']
    passwordin = request.POST['password']
    password = User.objects.filter(name = name) #取出的是objct
    if len(password) == 0:
        flag = True
        return render(request, 'no_name.html' )
    user_id = password[0].user_id
    password = password[0].password

    context = {}
    context['name'] = name
    context['passwordin'] = passwordin
    context['password'] = password
    if passwordin == password:
        return render(request , 'success_login.html',{"user":context})
    else:
        return render(request, 'loss_login.html')
    # contex['name'] = request.POST['name']
    # return render(request , 'success_login.html' , {"contex" :

def regist(request):
    ##########################
    #注册成功后放入数据库进行保存  #
    #!!!!!!!验证码问题继续研究   #
    #验证码已经在day2被我砍掉了！ #
    ##########################

    # contex['name'] = request.POST['name']
    # contex['password'] = request.POST['pass']
    name = request.POST['name']
    password =  request.POST['pass']
    user = User(name=name , password=password)
    user.save()
    return render(request , "success_regist.html")


def users_team(request):
    ##########################
    # day3的任务：            #
    #                        #
    # 完成use_team页面        #
    # 数据库数据整合并传入页面数据#
    # 完美的显示这些数据        #
    # to be continue         #
    ##########################
    context = {}
    user_name = name
    players_obj = User_player.objects.filter(user_id_id = user_id)
    # print(players_obj[0].player_id_id)
    # player = Player.objects.filter(id = players_obj[0].player_id_id)
    # print(player[0].position)
    players = []
    for i in range(len(players_obj)):
        id2player = players_obj[i].player_id_id
        player =  Player.objects.get(id = id2player)
        players.append(player)

    # print(players)
    context['players'] = players
    return render(request , "user.html" ,{"players":players , "user_name":user_name})

def add(request):
    ##################################
    #1.accept player's id            #
    #2.select player for his id      #
    #3.select user_team with uesr_id #
    #4.add new player in user_team   #
    #                                #
    #                                #
    #                                #
    #                                #
    ##################################
    # res = request.POST["a"] #{a:b}
    # user = User.objects.filter(user_id = res)
    # user = user[0].password
    #
    # contex = {"res":user}
    global user_id, name
    player_id = request.POST["id"]
    player = Player.objects.filter(id = player_id)
    if len(player) == 0:
        contex = {"notice" : "为查询到该球员"}
    else:
        contex = {"notice" : "添加成功"}
        user_player = User_player(user_id_id=user_id , player_id_id=player_id)
        user_player.save()

    return HttpResponse(json.dumps(contex) , content_type="application/type")


def delete(request):
    ###################################
    # 1.accept player's id            #
    # 2.select player for his id      #
    # 3.select user_team with uesr_id #
    # 4.add new player in user_team   #
    #                                 #
    #                                 #
    #                                 #
    #                                 #
    ###################################
    global user_id, name
    player_id = request.POST["id"]
    player = Player.objects.filter(id=player_id)
    if len(player) == 0:
        contex = {"notice": "id输入错误"}
    else:
        user_player = User_player.objects.filter(player_id_id=player_id)
        if len(user_player) == 0:
            contex = {"notice": "您未获得此球员"}
        else:
            user_player.delete()
            contex = {"notice": "删除成功"}

    return HttpResponse(json.dumps(contex), content_type="application/type")

def select(request):
    global user_id, name
    player_id = request.POST["id"]
    player = Player.objects.filter(id=player_id)
    if len(player) == 0:
        contex = {"notice": "id输入错误"}
    else:
        # user_player = User_player.objects.get(player_id_id=player_id)
        # user_player = [user_player]
        # user_player = serializers.serialize("json" , user_player)
        # contex = {"player" : user_player}
        # player = [player]
        player = serializers.serialize("json", player)
        contex = {"player": player}

    return HttpResponse(json.dumps(contex), content_type="application/type")

def show(request):
    context = {}
    user_name = name
    players_obj = User_player.objects.filter(user_id_id=user_id)
    # print(players_obj[0].player_id_id)
    # player = Player.objects.filter(id = players_obj[0].player_id_id)
    # print(player[0].position)
    players = []
    for i in range(len(players_obj)):
        id2player = players_obj[i].player_id_id
        player = Player.objects.get(id=id2player)
        players.append(player)
    # print(players)
    # context['players'] = players
    players = serializers.serialize("json" , players)
    context = {"players" : players}

    return HttpResponse(json.dumps(context), content_type="application/type")

def AI(request):

    ##############################################
    #     # 根据总分，利用K-means聚成3类                   #
    #     # 黑卡，金卡，银卡                              #
    #     # 分别显示每个类别的前3个球员                     #
    #     #                                            #
    #     #                                            #
    #     ##############################################
    # players = []
    # for i in range(len(players_obj)):
    #     id2player = players_obj[i].player_id_id
    #     player = Player.objects.get(id=id2player)
    #     players.append(player)
    #
    # # print(players)
    # context['players'] = players
    players = []
    for i in range(0,3):

        player_obj = Pre_Player.objects.filter(classify=i)

        for j in range(len(player_obj)):
            players.append(player_obj[j])
        # if i == 0:
        #     context["player0"] = players
        # elif i == 1:
        #     context["player1"] = players
        # elif i == 2:
        #     context["player2"] = players
    return render(request , "AIselect.html" , {"players":players})

# def classify(request):
#
#     # 守门员 GK
#     # 后场 CB LB LWB RB RWB
#     # 中场 CAM CDM LM RM
#     # 前场 CF CM ST
#
#     ##############################################
#     # 1.查找该用户的所有球员，调取位置信息“|之前”，统计   #
#     # 前中后场以及门将，缺什么推荐什么                  #
#     # 2.根据overall从高到低，推荐显示前3个             #
#     #                                            #
#     #                                            #
#     #                                            #
#     #                                            #
#     #                                            #
#     ##############################################
#
#     return render(request , "classify.html")

