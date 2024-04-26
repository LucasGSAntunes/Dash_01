from django.contrib import admin
from django.urls import path
from Dash.views import login, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login),
    path('register/', register),
]
