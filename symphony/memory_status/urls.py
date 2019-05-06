from django.urls import path, include, re_path
from .views import Login
from .views import Status

app_name = "memory_status"

urlpatterns = [
    re_path('^login', Login.as_view(), name='system-ui'), #Loads the UI
    re_path('^status/$', Status.as_view(), name='status') #Loads the Status Table
]