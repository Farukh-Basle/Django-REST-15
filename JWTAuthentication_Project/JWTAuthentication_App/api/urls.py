
from django.urls import path,include
from  JWTAuthentication_App.api  import  views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('employees', views.EmployeeModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


