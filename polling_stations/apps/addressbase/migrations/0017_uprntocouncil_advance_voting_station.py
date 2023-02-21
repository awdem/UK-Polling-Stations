# Generated by Django 3.2.5 on 2022-03-02 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("pollingstations", "0016_advancevotingstation"),
        ("addressbase", "0016_join_uprntocouncil_to_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="uprntocouncil",
            name="advance_voting_station",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="pollingstations.advancevotingstation",
            ),
        ),
    ]
