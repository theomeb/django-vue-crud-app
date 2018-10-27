from django.db import models

# Create your models here.
class Confidentiality(models.Model):
    name = models.CharField(max_length=255, null=False)
    total_docs = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.name, self.total_docs)