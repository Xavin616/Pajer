from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Source(models.Model):
    name = models.CharField(max_length=200)
    feed = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Headline(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    description = models.CharField(max_length=3500)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    date = models.CharField(max_length=200)
    pubDate = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title