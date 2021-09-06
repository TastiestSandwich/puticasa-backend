from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HouseSerializer
from .models import House


# Create your views here.

class HouseView(viewsets.ModelViewSet):
    serializer_class = HouseSerializer
    queryset = House.objects.all()
