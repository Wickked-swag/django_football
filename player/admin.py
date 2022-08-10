from django.contrib import admin
from .models import Player,User,User_team,User_player,Pre_Player
# Register your models here.

#class playerAdmin(admin.ModelAdmin):


class PlayerInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'player_name', 'nationality', 'position', 'overall', 'team')
    list_filter = ('nationality', 'team')

class RelationAdmin(admin.ModelAdmin):
    raw_id_fields = ["user_id","player_id"]

class RelationAdmin2(admin.ModelAdmin):
    raw_id_fields = ["user_id"]

#admin.site.register(player)
admin.site.register(Player , PlayerInstanceAdmin)
admin.site.register(User)
admin.site.register(User_team , RelationAdmin2)
admin.site.register(User_player , RelationAdmin)
admin.site.register(Pre_Player)
