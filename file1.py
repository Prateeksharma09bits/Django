# signals.py
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    print("Signal received, starting heavy computation...")
    time.sleep(5)  # Simulate long task
    print("Signal handler done.")

# In some view or management command
def create_user():
    print("Creating user...")
    User.objects.create(username="test_user")
    print("User created, but signal handler hasn't finished yet.")
    
# Output when the user is created:
# Creating user...
# Signal received, starting heavy computation...
# [5 second delay]
# Signal handler done.
# User created, but signal handler hasn't finished yet.
