from django.db import models
class Album(models.Model):
    artist = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    logo = models.ImageField(default='song_logo/swaglogo1.jpg',upload_to='song_logo')
    musicfile = models.FileField(upload_to='musicfile')
    slug = models.SlugField(default='')

    def __str__(self):
        return self.title

