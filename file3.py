# signals.py
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    if transaction.get_connection().in_atomic_block:
        print("Signal handler running inside a transaction.")
    else:
        print("Signal handler running outside of a transaction.")

# In some view or management command
@transaction.atomic
def create_user():
    print("Starting transaction and creating user...")
    User.objects.create(username="test_user")
    print("User created, signal should be in the same transaction.")

# Output:
# Starting transaction and creating user...
# Signal handler running inside a transaction.
# User created, signal should be in the same transaction.
