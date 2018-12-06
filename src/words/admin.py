from django.contrib import admin


# Register your models here.
from .models import Language, Word

admin.site.register(Language)
admin.site.register(Word)
