from django.shortcuts import render
from .serializers import *
from rest_framework import generics,viewsets 
from .models import *

# Create your views here.

class CategoryList(generics.ListCreateAPIView):
    queryset =  Category.objects.all()
    serializer_class = CategorySerializer
