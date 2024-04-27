# Generated by Django 4.2.6 on 2024-04-17 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("GradCam", "0002_userimage"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="images/")),
                ("upload_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
