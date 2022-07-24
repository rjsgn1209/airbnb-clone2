from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    list_display = ("__str__", "create")


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):

    list_display = ("__str__", "count_message", "count_participants")

    filter_horizontal = ("participants",)
