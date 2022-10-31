from email.policy import default
from django.db import models
import uuid

def upload_image_formater(instance, filename):
    return f"{str(uuid.uuid4())}-{filename}"

class Notice(models.Model):
    image = models.ImageField(upload_to=upload_image_formater, blank=True, null=True)
    title = models.CharField(max_length=60)
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    date = models.DateField()
    highlighted = models.BooleanField(default=False)
    photo = models.ImageField(upload_to=upload_image_formater, blank=True, null=True)
    author = models.CharField(max_length=60, blank=True, null=True)
    bibliography = models.TextField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Newsletter(models.Model):
    email = models.CharField(max_length=90)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
    
class Comment(models.Model):
    photo = models.ImageField(upload_to=upload_image_formater, blank=True, null=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30, blank=True, null=True)
    comment = models.TextField(max_length=250)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name + " " + self.surname
    