from rest_framework.authentication import BaseAuthentication
from nomi_match.models import ParticipantIdentities

class ParticipantTokenAuth(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get("X-Participant-Token")
        if not token:
            return None
        identity = ParticipantIdentities.objects.filter(
            participant_token=token
        ).first()
        if not identity:
            return None
        return (identity, None)
