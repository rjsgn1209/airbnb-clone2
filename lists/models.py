from django.db import models
from core import models as core_models

# Create your models here.


class List(core_models.TimeStempedModel):

    name = models.CharField(max_length=80)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    rooms = models.ManyToManyField("rooms.Room", blank=True)

    def __str__(self):
        return self.name

    def count_room(self):
        return self.rooms.count()

    count_room.short_description = "Number of Room"
