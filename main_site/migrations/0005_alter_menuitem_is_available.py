# Generated by Django 4.1 on 2023-01-17 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_site", "0004_remove_menuitem_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menuitem",
            name="is_available",
            field=models.BooleanField(default=True),
        ),
    ]
