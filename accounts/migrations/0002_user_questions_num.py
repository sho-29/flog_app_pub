# Generated by Django 5.0.7 on 2024-07-15 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='questions_num',
            field=models.IntegerField(default=0),
        ),
    ]
