import django
import pandas as pd
from celery import Celery
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","django_football.settings")
django.setup()
from player.models import User,Player,User_team


def load_data():
    csv_data = pd.read_csv("../player/lib/data.csv")

    return csv_data

def load_player(players):
    for i in range(len(players)):
        player = players.iloc[i]
        player = Player(id=player.player_id, player_name=player.player_name, nationality=player.nationality, position=player.position,
                        overall=player.overall, age=player.age, hits=player.hits, potential=player.potential,
                        team=player.team)
        player.save()
        print(player.player_name)



data = load_data()
load_player(data)
# Player.objects.all().delete()
# print(data.head())