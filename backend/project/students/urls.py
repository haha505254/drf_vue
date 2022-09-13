
from django.urls import path,include


from rest_framework import routers
from .views import StutentsViewSet

routers = routers.DefaultRouter()
routers.register('students',StutentsViewSet)

urlpatterns = routers.urls