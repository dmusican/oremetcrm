from django.contrib import admin
from .models import Family
from .models import Person

admin.site.register(Family)
admin.site.register(Person)
