# Generated by Django 4.1 on 2023-01-20 05:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kitchen", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="dish",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recipe",
                to="kitchen.dish",
            ),
        ),
    ]