from django.contrib import admin
from .models import Source, Headline, Category,  User, Follow

class SourceAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

# Register your models here.
admin.site.register(Source, SourceAdmin)
admin.site.register(Headline)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Follow)