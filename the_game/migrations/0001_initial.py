# Generated by Django 4.1.3 on 2022-11-23 17:54

from django.db import migrations, models
import the_game.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='side_stack_game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_state', models.JSONField(default=the_game.models.side_stack_game.initialize_board)),
                ('player_1', models.CharField(default='', max_length=100)),
                ('player_2', models.CharField(default='', max_length=100)),
                ('player_1_name', models.CharField(default='', max_length=256)),
                ('player_2_name', models.CharField(default='', max_length=256)),
                ('num_player_1_connection', models.IntegerField(default=0)),
                ('num_player_2_connection', models.IntegerField(default=0)),
                ('game_complete', models.BooleanField(default=False)),
                ('against_bot', models.BooleanField(default=False)),
                ('game_winner', models.CharField(blank=True, max_length=1, null=True)),
            ],
        ),
    ]
