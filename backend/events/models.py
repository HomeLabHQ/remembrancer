from django.db import models
from django.utils import timezone

from core.models import TimeStampedModel, TitleDescriptionModel


class Event(TitleDescriptionModel, TimeStampedModel):
    is_public = models.BooleanField(default=False)
    author = models.ForeignKey(
        "authentication.User",
        on_delete=models.CASCADE,
        related_name="events",
    )
    color = models.CharField(max_length=7, default="#ffffff")
    date = models.DateField(default=timezone.now)

    class Meta:
        ordering = ("-pk",)
        db_table = "events"
        verbose_name = "events"
        verbose_name_plural = "events"
