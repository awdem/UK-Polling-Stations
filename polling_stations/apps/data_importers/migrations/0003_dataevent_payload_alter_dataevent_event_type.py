# Generated by Django 4.2.10 on 2024-02-13 15:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("data_importers", "0002_dataevent"),
    ]

    operations = [
        migrations.AddField(
            model_name="dataevent",
            name="payload",
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name="dataevent",
            name="event_type",
            field=models.CharField(
                choices=[
                    ("IMPORT", "Import script run"),
                    ("TEARDOWN", "Council data torn down"),
                    ("SET_STATION_VISIBILITY", "Station visibility changed"),
                ]
            ),
        ),
    ]
