# Generated by Django 4.1 on 2023-01-17 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0004_alter_orderitem_quantity"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
