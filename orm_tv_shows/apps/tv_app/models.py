from __future__ import unicode_literals

from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 3:
            errors["name"] = "Title must be longer than 2. Sorry \'V\'"
        if len(postData['network']) < 4:
            errors["network"] = "Network must be longer than 3. Srry WB."
        if len(postData["description"]) < 11:
            errors["description"] = "Description must be longer than 10, please tell me more."
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=25)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

# Create your models here.
