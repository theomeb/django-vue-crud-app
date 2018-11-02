from django.contrib import admin
from .models import Confidentiality, Language, Doctype

# Register your models here.
admin.site.register(Confidentiality)
admin.site.register(Language)
admin.site.register(Doctype)