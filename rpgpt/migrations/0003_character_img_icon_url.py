# Generated by Django 4.2.1 on 2023-05-06 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpgpt', '0002_alter_character_character_class_alter_character_hp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='img_icon_url',
            field=models.CharField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpA_2RZ3HMN0pbKHXoNd4UpnBoxkSccoUkUg&usqp=CAU', max_length=400),
        ),
    ]