import datetime

import factory
import factory.fuzzy

from events.models import Event


class EventFactory(factory.django.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText()
    description = factory.fuzzy.FuzzyText()
    date = factory.fuzzy.FuzzyDate((datetime.date(2008, 1, 1)))
    color = factory.fuzzy.FuzzyText(length=7)

    class Meta:
        model = Event
