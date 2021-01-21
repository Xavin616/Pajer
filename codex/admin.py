from django.contrib import admin
from .models import Source, Headline, Category,  User, Follow

# Register your models here.
admin.site.register(Source)
admin.site.register(Headline)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Follow)