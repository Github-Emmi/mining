
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class A_User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    wallet_address = models.CharField(max_length=500, blank=True)
    phone_no = models.CharField(max_length=15, blank=True)
    username = models.CharField(max_length=100, unique=True)


    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['wallet_address']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


from django.db import models
from django.contrib.auth.models import AbstractUser


amount = (
    ('none', 'Select Amount'),
    ('100', '100'),
    ('500', '500'),
    ('600', '600'),
    ('1000', '1,000'),
    ('2000', '2,000'),
    ('5000', '5,000'),
)

method = (
    ('none', 'Select Method'),
    ('BTC', 'Bitcoin'),
    ('ETH', 'Ethereum'),
    ('LCN', 'LiteCoin'),
    ('DOGE', 'DogeCoin'),
    ('DASH', 'Dash'),
    ('ZCASH', 'ZCash'),
)

class User(AbstractUser):
    wallet_address = models.CharField(max_length=30, blank=True)
    phone_no = models.CharField(max_length=25, blank=True)
    fund_method = models.CharField(max_length=7, choices=method, default='none')
    fund_amount = models.CharField(max_length=15, choices=amount, default='none')
    withdrawal_amount = models.CharField(max_length=15, null=True)
    withdrawal_method = models.CharField(max_length=15, choices=method, default='none')


    USERNAME_FIELD = 'username'