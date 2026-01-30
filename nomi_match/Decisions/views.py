from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from nomi_match.models import Decisions

class DecideView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, event_id):
        Decisions.objects.update_or_create(
            event_id=event_id,
            defaults={"slot_id": request.data["slot_id"]}
        )
        return Response({"decided": True})
