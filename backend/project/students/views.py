from django.shortcuts import render
from django.http import JsonResponse
from .models import Student
from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer


class StutentsViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


