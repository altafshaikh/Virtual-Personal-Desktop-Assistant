from rest_framework import serializers
from . models import employee
from . models import command


class employeeSerializer(serializers.ModelSerializer):

	class Meta:
		model = employee
		fields = '__all__'

class commandSerializer(serializers.ModelSerializer):

	class Meta:
		model = command
		fields = '__all__'
