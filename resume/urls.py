from django.urls import path

from .views import modelo

urlpatterns = [
    path("modelo/", modelo, name="modelo"),
]