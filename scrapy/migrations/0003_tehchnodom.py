# Generated by Django 4.0.4 on 2022-05-31 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scrapy", "0002_lalafo"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tehchnodom",
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
                ("image", models.ImageField(upload_to="")),
                ("title", models.CharField(max_length=255)),
                ("price", models.CharField(max_length=100)),
            ],
        ),
    ]
