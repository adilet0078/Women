from django.contrib import admin
from django.db import models

from .models import Women, Category

admin.site.register(Women)
admin.site.register(Category)
