# Generated by Django 4.0.4 on 2022-09-08 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapy', '0007_alter_tehchnodom_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchs',
            name='price',
            field=models.CharField(max_length=250, null=True),
        ),
    ]