from django.shortcuts import render
from rest_framework import viewsets
from .models import Agricultor
from .serializers import AgricultorSerializer

class AgricultorViewSet(viewsets.ModelViewSet):
    queryset = Agricultor.objects.all().order_by('-id')
    serializer_class = AgricultorSerializer
