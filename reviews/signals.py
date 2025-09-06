from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import Profile, Review

# Create profile automatically when user registers
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Save profile if updated
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# Send email when new review is added
@receiver(post_save, sender=Review)
def notify_new_review(sender, instance, created, **kwargs):
    if created:
        subject = f"New Review for {instance.book.title}"
        message = f"{instance.user.username} rated {instance.rating}/5\n\n{instance.comment}"
        send_mail(
            subject,
            message,
            'admin@bookreview.com',  # from email
            ['admin@bookreview.com'],  # to email (can be dynamic)
            fail_silently=True,
        )
