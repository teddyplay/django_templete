# Generated by Django 4.0.4 on 2022-06-02 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="birth_date",
            field=models.DateField(null=True),
        ),
    ]
