from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HouseSerializer, ResidentSerializer
from .models import House, Resident


# Create your views here.

class HouseView(viewsets.ModelViewSet):
    serializer_class = HouseSerializer
    queryset = House.objects.all()


class ResidentView(viewsets.ModelViewSet):
    serializer_class = ResidentSerializer
    queryset = Resident.objects.all()
