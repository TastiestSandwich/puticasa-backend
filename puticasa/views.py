from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HouseSerializer, ResidentJSONSerializer
from .models import House, Resident
from users.models import User
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from django.views import generic


# Create your views here.

class HouseView(viewsets.ModelViewSet):
    serializer_class = HouseSerializer
    queryset = House.objects.all()


class ResidentView(viewsets.ModelViewSet):
    serializer_class = ResidentJSONSerializer

    def get_queryset(self):
        user = self.request.user
        return user.residents.all()

