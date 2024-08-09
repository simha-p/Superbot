from django.db import models

class Hero(models.Model):
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='hero_images/')
  background_image = models.ImageField(upload_to='hero_backgrounds/')
  icon = models.ImageField(upload_to='hero_icons/')

  def __str__(self):
      return self.name