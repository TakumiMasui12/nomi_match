from rest_framework.views import APIView
from rest_framework.response import Response
from nomi_match.models import ScheduleSlots, Availabilities

class SlotCreateView(APIView):
    def post(self, request):
        slot = ScheduleSlots.objects.create(
            event_id=request.data["event_id"],
            start_at=request.data["start_at"],
            end_at=request.data["end_at"]
        )
        return Response({"slot_id": slot.id})

class AvailabilityView(APIView):
    def post(self, request):
        Availabilities.objects.update_or_create(
            slot_id=request.data["slot_id"],
            participant_identity=request.user,
            defaults={"status": request.data["status"]}
        )
        return Response({"ok": True})
