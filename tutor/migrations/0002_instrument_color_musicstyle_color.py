# Generated by Django 4.2.9 on 2024-01-13 15:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tutor", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="instrument",
            name="color",
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AddField(
            model_name="musicstyle",
            name="color",
            field=models.CharField(max_length=6, null=True),
        ),
    ]
