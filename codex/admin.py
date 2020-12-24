from django.contrib import admin
from .models import Source, Headline, Category

# Register your models here.
admin.site.register(Source)
admin.site.register(Headline)
admin.site.register(Category)