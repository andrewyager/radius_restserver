from django.db import models
from django.contrib.auth.models import AbstractUser

class RadiusUser(AbstractUser):
	pass

RadiusUser._meta.get_field('username').max_length = 255
