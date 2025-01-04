import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import connection, transaction

@receiver(post_save, sender=User)
def signal_handler(sender, instance, **kwargs):
    print(f"Signal handler thread: {threading.current_thread().name}")
    print("Signal handler: Transaction status before insertion:", connection.in_atomic_block)
    # Insert data into example_table
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO example_table (data) VALUES ('Signal Data')")
    print("Signal handler: Data inserted into 'example_table'")
