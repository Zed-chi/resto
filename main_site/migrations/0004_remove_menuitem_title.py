# Generated by Django 4.1 on 2023-01-17 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main_site", "0003_alter_roomtable_number"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="menuitem",
            name="title",
        ),
    ]