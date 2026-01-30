from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from nomi_match.models import Events
from .service import generate_invite_token

class EventCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        event = Events.objects.create(
            organizer=request.user,
            title=request.data["title"],
            budget_hint=request.data.get("budget"),
            invite_token=generate_invite_token()
        )
        return Response({
            "event_id": event.id,
            "invite_url": f"/join/{event.invite_token}"
        })

class InviteInfoView(APIView):
    def get(self, request, token):
        event = Events.objects.filter(invite_token=token).first()
        if not event:
            return Response(status=404)
        return Response({"title": event.title})
