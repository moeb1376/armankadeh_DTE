from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as Django_UserManager
# Create your models here.
from django.utils import timezone


class MyUser(AbstractUser):
    # picture = models.ImageField()
    phone_number = models.CharField(help_text='Like 09XXXXXXXXX', max_length=11)
    is_tagger = models.BooleanField(default=True)

    def __str__(self):
        return self.username


class UserManager(Django_UserManager):

    def create_superuser(self, username, email, password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        email = UserManager.normalize_email(email)
        user = MyUser(username=username, email=email,
                      is_staff=True, is_active=True, is_superuser=True,
                      last_login=now, date_joined=now)

        user.set_password(password)
        user.save(using=self._db)
