# Generated by Django 4.0.4 on 2022-05-09 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tie_breaker', models.IntegerField(verbose_name=389)),
                ('main_wow_character', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('dnd_experience', models.TextField()),
                ('describe_your_dnd_character', models.TextField()),
                ('player_gender', models.CharField(max_length=50)),
                ('describe_player_personality', models.TextField()),
                ('guild_leadership', models.BooleanField()),
            ],
        ),
    ]