# Generated by Django 3.2.5 on 2022-01-11 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("file_uploads", "0003_store_csv_file_encoding"),
    ]

    operations = [
        migrations.AddField(
            model_name="file",
            name="version",
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name="upload",
            name="election_date",
            field=models.DateField(null=True),
        ),
    ]
