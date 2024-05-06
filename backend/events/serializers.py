from django.db import transaction
from rest_framework import serializers

from authentication.serializers import BaseUserSerializer
from events.models import Event


class BaseEventSerializer(serializers.ModelSerializer):
    date = serializers.DateField()
    author = BaseUserSerializer(read_only=True)

    class Meta:
        model = Event
        fields = (
            "id",
            "title",
            "color",
            "is_public",
            "date",
            "author",
        )
        read_only_fields = (
            "id",
            "author",
        )


class EventSerializer(BaseEventSerializer):
    title = serializers.CharField(max_length=255)

    class Meta(BaseEventSerializer.Meta):
        fields = (
            *BaseEventSerializer.Meta.fields,
            "description",
        )

    @transaction.atomic
    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        return super().create(validated_data)
