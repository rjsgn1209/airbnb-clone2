from email.policy import default
from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models

# Create your models here.


class AbstractItem(core_models.TimeStempedModel):
    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    class Meta:
        verbose_name = "Room Type"
        ordering = ["create"]


class Amenities(AbstractItem):
    class Meta:
        verbose_name_plural = "Amenities"


class Facilities(AbstractItem):
    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStempedModel):

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStempedModel):

    """Room Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )
    room_type = models.ForeignKey(
        "RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    amenities = models.ManyToManyField("Amenities", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facilities", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def save(self, *arg, **kwarg):
        self.city = str.capitalize(self.city)
        super().save(*arg, **kwarg)

    def __str__(self):
        return self.name

    def total_rating(self):
        all_ratings = []
        for review in self.reviews.all():
            all_ratings.append(review.rating_average())
        total = sum(all_ratings) / len(all_ratings)
        return total
