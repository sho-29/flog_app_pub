# Generated by Django 5.0.7 on 2024-07-21 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player_result',
            name='flog_rate',
            field=models.FloatField(default=0),
        ),
    ]
