# Generated by Django 4.0.4 on 2022-06-02 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_customuser_birth_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="birth_date",
        ),
    ]
