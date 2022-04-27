from django.contrib import admin
from .models import Person,Portfolio,Experience,Education,Language

admin.site.register(Person)
admin.site.register(Portfolio)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Language)