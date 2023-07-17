# Generated by Django 4.2.3 on 2023-07-17 05:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("aqua_tally_api", "0002_alter_goalmodel_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="goalmodel",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="goalmodel",
            name="date",
            field=models.DateField(auto_now_add=True, db_index=True),
        ),
    ]
