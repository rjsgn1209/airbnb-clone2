from django.db import models
from core import models as core_models

# Create your models here.


class Conversation(core_models.TimeStempedModel):

    title = models.CharField(max_length=80, default="")
    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        return self.title

    def count_message(self):
        return self.messages.count()

    count_message.short_description = "Nuber of Messages"

    def count_participants(self):
        return self.participants.count()

    count_participants.short_description = "Number of Participants"


class Message(core_models.TimeStempedModel):

    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says: {self.message}"
