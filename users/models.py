from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.

class User(AbstractUser):
    username_validator = ASCIIUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 ASCII characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    REQUIRED_FIELDS = []


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    