# Generated by Django 2.2.16 on 2020-12-09 15:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("addressbase", "0015_delete_blacklist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="uprntocouncil",
            name="uprn",
            field=models.OneToOneField(
                db_column="uprn",
                max_length=12,
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to="addressbase.Address",
            ),
        ),
    ]
