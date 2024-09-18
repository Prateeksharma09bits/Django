# signals.py
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    print(f"Signal handler running in thread: {threading.current_thread().name}")

# In some view or management command
def create_user():
    print(f"Main code running in thread: {threading.current_thread().name}")
    User.objects.create(username="test_user")

# Output:
# Main code running in thread: MainThread
# Signal handler running in thread: MainThread
