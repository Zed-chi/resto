# Generated by Django 4.1 on 2023-01-20 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="started_to_cook",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
