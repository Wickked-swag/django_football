from django.db import models
from django.contrib.auth.models import AbstractUser

class Player(models.Model):
    id = models.IntegerField(primary_key=True)
    player_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    overall = models.IntegerField()
    age = models.IntegerField()
    hits = models.IntegerField()
    potential = models.IntegerField()
    team = models.CharField(max_length=50)

    def __str__(self):
        return self.player_name

    class Meta:
        db_table = "Player"

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=16)
    def __str__(self):
        return self.name
    class Meta:
        db_table = "User"

class User_team(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    team_name = models.CharField(max_length=50 , default="")
    def __str__(self):
        return self.team_name

    class Meta:
        db_table = "User_team"

class User_player(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return self.player_id_id

    class Meta:
        db_table = "User_player"

class Pre_Player(models.Model):
    id = models.IntegerField(primary_key=True)
    player_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    overall = models.IntegerField()
    age = models.IntegerField()
    hits = models.IntegerField()
    potential = models.IntegerField()
    team = models.CharField(max_length=50)
    classify = models.IntegerField()
    def __str__(self):
        return self.player_name

    class Meta:
        db_table = "Pre_Player"