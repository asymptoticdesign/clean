import datetime
from django.db import models
from django.contrib.auth.models import User
from tagging.fields import Tag, TagField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=512)
    slug = models.SlugField(unique=True,help_text="Suggested slug value.  Must be unique.")
    created_date = models.DateField(default=datetime.datetime.now)
    subject = models.ForeignKey('Subject')
    tags = TagField()

    instructions = models.TextField(help_text="Instructions for the assignment.")
    references = models.TextField(help_text="Enter any references you would like to provide.");

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/projects/%s/" % self.slug

class Sketch(models.Model):
    project = models.ForeignKey('Project')
    slug = models.SlugField()
    created_date = models.DateField(default=datetime.datetime.now)
    author = models.ForeignKey(User)

    content = models.TextField()
    sparkles = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return "/projects/%s/" % self.slug

class Subject(models.Model):
    title = models.CharField(max_length=250,help_text="Maximum 250 characters")
    slug = models.SlugField(unique=True,help_text="Suggested value automatically generated from title. Must be unique.")
    description = models.TextField()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/subjects/%s/" % self.slug
