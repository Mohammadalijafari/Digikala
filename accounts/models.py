from datetime import timezone

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail


# Create your models here.
class UserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(email, password, **extra_fields)


class ActiveUserManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(
        verbose_name=_("First name"),
        max_length=150,
        blank=True,
    )
    last_name = models.CharField(
        verbose_name=_("Last name"),
        max_length=150,
        blank=True,
    )
    email = models.EmailField(
        verbose_name=_("Email"),
        max_length=254,
        unique=True,
        blank=True,
    )
    mobile = models.CharField(
        verbose_name=_("Mobile number"),
        max_length=11,
        unique=True,
        blank=True,
        null=True,
    )
    is_staff = models.BooleanField(
        verbose_name=_("Is staff"),
        default=True,
        help_text=_(
            "Designates whether the user can log into this admin site. "
        ),
    )
    is_active = models.BooleanField(
        verbose_name=_("Is active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        )
    )
    date_joined = models.DateTimeField(
        verbose_name=_("Date joined"),
        default=timezone.now,
    )
    objects = UserManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Return the short name for the user.
        """
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)


class ActiveUser(User):
    objects = ActiveUserManager()

    class Meta:
        proxy = True
