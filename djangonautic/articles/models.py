from django.db import models

# everytime make models do the below command
# python manage.py makemigrations
# python manage.py migrate


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.jpg', blank=True)
    # add in author later

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'
