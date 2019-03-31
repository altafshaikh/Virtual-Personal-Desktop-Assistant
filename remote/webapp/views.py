from django.shortcuts import render
from rest_framework import viewsets
from . models import employee, command
from . serializers import employeeSerializer
from . serializers import commandSerializer
#from django.utils.decorators import method_decorator


class employeeList(viewsets.ModelViewSet):
	queryset = employee.objects.all()
	serializer_class = employeeSerializer

class commandList(viewsets.ModelViewSet):
	queryset = command.objects.all()
	serializer_class = commandSerializer