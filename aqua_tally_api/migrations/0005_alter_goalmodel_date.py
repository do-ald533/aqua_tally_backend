# Generated by Django 4.2.3 on 2023-07-17 06:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("aqua_tally_api", "0004_alter_goalmodel_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="goalmodel",
            name="date",
            field=models.DateField(db_index=True),
        ),
    ]