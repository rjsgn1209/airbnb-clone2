from django.db import models

# Create your models here.
class TimeStempedModel(models.Model):

    """Time Stemped Model"""

    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
