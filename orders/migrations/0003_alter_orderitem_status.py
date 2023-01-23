# Generated by Django 4.1 on 2023-01-23 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_orderitem_started_to_cook"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderitem",
            name="status",
            field=models.CharField(
                choices=[
                    ("1", "Черновик"),
                    ("2", "В ожидании"),
                    ("3", "Готовится"),
                    ("4", "Готово"),
                    ("5", "Доставлено"),
                ],
                default="1",
                max_length=50,
            ),
        ),
    ]