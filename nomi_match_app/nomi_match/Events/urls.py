from django.urls import path
from .views import EventCreateView, InviteInfoView

urlpatterns = [
    path("", EventCreateView.as_view()),
    path("invite/<str:token>/", InviteInfoView.as_view()),
]
