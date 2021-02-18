from django.db import models

# Create your models here.
class Project(models.Model):
    image = models.ImageField(upload_to='uploaded_images')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class Message(models.Model):
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
