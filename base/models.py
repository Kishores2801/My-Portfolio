
from django.db import models
import uuid
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField()
    body =RichTextUploadingField()
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True) 
    #github_url = models.URLField(null=True,blank=True)
    #Deepnote_url = models.URLField(null=True,blank=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField()
    #context=models.TextField()
    body = RichTextUploadingField()
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True) 
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)


    def __str__(self) :
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True,
                          primary_key=True, editable=False)


    def __str__(self):
        return self.name



