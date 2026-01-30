from ics import Calendar, Event as IcsEvent
from django.http import HttpResponse
from nomi_match.models import Decisions

def event_ics(request, event_id):
    decision = Decisions.objects.get(event_id=event_id)
    cal = Calendar()
    e = IcsEvent()
    e.name = decision.event.title
    e.begin = decision.slot.start_at
    e.end = decision.slot.end_at
    cal.events.add(e)
    return HttpResponse(
        cal.serialize(),
        content_type="text/calendar"
    )
