# Generated by Django 3.1.4 on 2020-12-18 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0005_auto_20201217_0953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_team',
            name='player_id',
        ),
        migrations.CreateModel(
            name='User_player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.player')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.user')),
            ],
            options={
                'db_table': 'User_player',
            },
        ),
    ]
