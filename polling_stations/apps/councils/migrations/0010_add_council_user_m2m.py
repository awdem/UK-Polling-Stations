# Generated by Django 3.2.5 on 2022-01-13 12:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("councils", "0009_alter_council_name_translated"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserCouncils",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "council",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="councils.council",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "User Councils",
            },
        ),
        migrations.AddField(
            model_name="council",
            name="users",
            field=models.ManyToManyField(
                through="councils.UserCouncils", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
