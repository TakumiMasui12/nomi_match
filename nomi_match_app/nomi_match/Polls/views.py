from rest_framework.views import APIView
from rest_framework.response import Response
from nomi_match.models import PollVotes

class VoteView(APIView):
    def post(self, request):
        PollVotes.objects.update_or_create(
            poll_id=request.data["poll_id"],
            participant_identity=request.user,
            defaults={"option_id": request.data["option_id"]}
        )
        return Response({"voted": True})