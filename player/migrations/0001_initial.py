# Generated by Django 3.1.4 on 2020-12-14 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='player',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('overall', models.IntegerField()),
                ('age', models.IntegerField()),
                ('hits', models.IntegerField()),
                ('potential', models.IntegerField()),
                ('team', models.CharField(max_length=50)),
            ],
        ),
    ]
