import threading

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import transaction, connection

class Command(BaseCommand):
    help = "Test signals with transactions"

    def handle(self, *args, **kwargs):
        try:
            with transaction.atomic():
                print("Caller thread:", threading.current_thread().name)
                print("Caller: Transaction status before user save:", connection.in_atomic_block)
                user = User.objects.create(username="testuser")
                print("Caller: User saved, raising exception to roll back")
                raise Exception("Force rollback")
        except Exception as e:
            print("Caller: Transaction rolled back")
