# Generated by Django 3.2.12 on 2022-02-18 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DemoExtensionConfig",
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
                    "demo_field",
                    models.CharField(max_length=250, verbose_name="demo field"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
