# Generated by Django 4.2.3 on 2023-07-17 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("aqua_tally_api", "0003_goalmodel_id_alter_goalmodel_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="goalmodel",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="aqua_tally_api.usermodel",
            ),
        ),
    ]
