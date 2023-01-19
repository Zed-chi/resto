# Generated by Django 4.1 on 2023-01-19 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0007_remove_orderitem_menu_item_orderitem_dish"),
        ("main_site", "0005_alter_menuitem_is_available"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="menucategory",
            name="menu",
        ),
        migrations.RemoveField(
            model_name="menuitem",
            name="category",
        ),
        migrations.RemoveField(
            model_name="menuitem",
            name="dish",
        ),
        migrations.DeleteModel(
            name="Menu",
        ),
        migrations.DeleteModel(
            name="MenuCategory",
        ),
        migrations.DeleteModel(
            name="MenuItem",
        ),
    ]
