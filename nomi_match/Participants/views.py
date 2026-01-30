import secrets
from rest_framework.views import APIView
from rest_framework.response import Response
from nomi_match.models import ParticipantIdentities, EventParticipants

class JoinEventView(APIView):
    def post(self, request, token):
        identity = ParticipantIdentities.objects.create(
            participant_token=secrets.token_urlsafe(32)
        )
        EventParticipants.objects.create(
            event_id=request.data["event_id"],
            participant_identity=identity,
            display_name=request.data["display_name"]
        )
        return Response({
            "participant_token": identity.participant_token
        })
