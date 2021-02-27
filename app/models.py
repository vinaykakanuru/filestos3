from django.db import models

# Create your models here.


class File(models.Model):

    file = models.FileField(null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.description
