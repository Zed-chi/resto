from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates initial role groups"

    def handle(self, *args, **kwargs):
        Group.objects.create(name="Admins")
        Group.objects.create(name="Cooks")
        Group.objects.create(name="Waiters")
        print("initial groupes created")
