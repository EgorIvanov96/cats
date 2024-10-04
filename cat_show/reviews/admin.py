from django.contrib import admin

from .models import Cats, Porode

admin.site.register(Cats)
admin.site.register(Porode)
admin.site.empty_value_display = 'Не задано'
