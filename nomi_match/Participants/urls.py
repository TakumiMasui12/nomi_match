from django.urls import path
from .views import JoinEventView

urlpatterns = [
    path("join/<str:token>/", JoinEventView.as_view()),
]
