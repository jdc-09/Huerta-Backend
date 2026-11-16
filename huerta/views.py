from django.shortcuts import render
from rest_framework import viewsets
from .models import Agricultor, Cultivo
from .serializers import AgricultorSerializer, CultivoSerializer

class AgricultorViewSet(viewsets.ModelViewSet):
    queryset = Agricultor.objects.all().order_by('-id')
    serializer_class = AgricultorSerializer

class CultivoViewSet(viewsets.ModelViewSet):
    queryset = Cultivo.objects.all().order_by('-id')
    serializer_class = CultivoSerializer