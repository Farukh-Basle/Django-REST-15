

from django.shortcuts import render,redirect
from JWTAuthentication_App.models import Employee
from JWTAuthentication_App.api.serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAdminUser

class EmployeeModelViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAdminUser,)







