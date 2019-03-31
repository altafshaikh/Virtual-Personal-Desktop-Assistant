from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
#from index import views


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('employees/',include("webapp.urls")),
    path('commands/',include("webapp.urls")),
    # path('signup/', views.SignUp.as_view(), name="signup"),
    # #spath('^accounts/', include("django.contrib.auth.urls")),
    # path('mode/',include("mode.urls")),
    path('',include("home.urls",namespace='home')),
    #path('^accounts/', include("accounts.urls", namespace="accounts")),
    #path('^accounts/', include("django.contrib.auth.urls")),
    
]
