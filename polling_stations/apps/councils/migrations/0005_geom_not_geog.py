# Generated by Django 2.2.10 on 2020-02-14 14:41
# Amended by Will on 2021-04-11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("councils", "0004_auto_20200203_1040"),
    ]

    operations = [
        migrations.RunSQL(
            'ALTER TABLE "councils_council" ALTER COLUMN "area" TYPE geometry(MULTIPOLYGON,4326) USING area::geometry(MultiPolygon,4326);'
        )
    ]
