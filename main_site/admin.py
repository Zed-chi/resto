from django.contrib import admin

from .models import Menu, MenuCategory, MenuItem, Room, RoomTable

admin.site.register(Room)
admin.site.register(RoomTable)
admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(MenuItem)
