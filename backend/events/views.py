from core.mixins import ListSerializerMixin
from django.db.models import Q
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from events.models import Event
from events.serializers import BaseEventSerializer, EventSerializer


class EventsViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    ListSerializerMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (IsAuthenticated,)
    list_serializer_class = BaseEventSerializer
    serializer_class = EventSerializer

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return Event.objects.filter(is_public=True)
        else:
            return Event.objects.filter(Q(author_id=self.request.user.id) | Q(is_public=True))
