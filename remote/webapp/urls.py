from django.urls import path
from django.conf.urls import include,url
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
#router.register('webapp',views.employeeList)
router.register('webapp',views.commandList)

urlpatterns = [
	path("",include(router.urls))
]
