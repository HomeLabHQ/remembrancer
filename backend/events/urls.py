from rest_framework.routers import SimpleRouter

from events.views import EventsViewSet

app_name = "events"
router = SimpleRouter()
router.register("events", EventsViewSet, basename="events")

urlpatterns = [*router.urls]
