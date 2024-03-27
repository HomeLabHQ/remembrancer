import typing

from authentication.models import User
from core.tests import CRUDTestCase
from django.test import TestCase

from events.models import Event
from events.tests.factories import EventFactory


class EventVewSetTest(CRUDTestCase, TestCase):
    base_view = "events:events"
    queryset = Event.objects.all()
    item_count = 100
    methods: typing.ClassVar = ["list", "retrieve", "update", "partial_update"]

    def setUp(self) -> None:
        self.user: User = self.create_and_login()
        for _ in range(self.item_count):
            EventFactory.create(author=self.user)
