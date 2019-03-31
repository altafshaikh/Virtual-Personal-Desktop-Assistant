from django.contrib import admin
from . models import command, employee
# Register your models here.

admin.site.register(employee)
admin.site.register(command)
