from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Source(models.Model):
    name = models.CharField(max_length=200)
    feed = models.URLField()
    image = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    '''class Meta:
        ordering = ['name']'''
    
    def __str__(self):
        return self.name

class Headline(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    description = models.CharField(max_length=3500, default="")
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True)
    like = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date']
    
class Follow(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    source = models.ManyToManyField(Source)
    
    def __str__(self):
        return f'{self.user.username}: {self.source.count()}'
    
    @property
    def source_count(self):
        return self.source.count()