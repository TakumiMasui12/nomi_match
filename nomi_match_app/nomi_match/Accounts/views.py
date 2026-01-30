from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class LoginView(APIView):
    def post(self, request):
        user = authenticate(
            username=request.data.get("login_id"),
            password=request.data.get("password")
        )
        if not user:
            return Response({"detail": "Invalid"}, status=401)
        login(request, user)
        return Response({"organizer_id": user.id})

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response(status=204)
