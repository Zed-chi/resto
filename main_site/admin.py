from django.contrib import admin

from .models import Room, RoomTable


admin.site.register(RoomTable)


class TableInline(admin.StackedInline):
    model = RoomTable


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    inlines = [TableInline,]