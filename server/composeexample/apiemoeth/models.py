from django.db import models

# Create your models here.
class Confidentiality(models.Model):
    name = models.CharField(max_length=255, null=False)
    total_docs = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.name, self.total_docs)

class Language(models.Model):
    short_name = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)
    total_docs = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {} - {}".format(self.short_name, self.name, self.total_docs)

class Doctype(models.Model):
    name = models.CharField(max_length=255, null=False)
    total_docs = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.name, self.total_docs)