# Generated by Django 4.1 on 2023-01-23 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0003_alter_orderitem_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="estimated_finish_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
