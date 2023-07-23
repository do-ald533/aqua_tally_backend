# Generated by Django 4.2.3 on 2023-07-23 04:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("aqua_tally_api", "0005_alter_goalmodel_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="goalmodel",
            name="goal",
        ),
        migrations.AddField(
            model_name="usermodel",
            name="goal",
            field=models.FloatField(default=0),
        ),
    ]