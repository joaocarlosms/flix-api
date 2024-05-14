from django.shortcuts import render
from rest_framework import generics
from actors.models import Actor
from actors.serializers import ActorSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermissions

class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
