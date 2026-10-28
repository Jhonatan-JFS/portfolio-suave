from django.urls import path
from . import views

app_name = "portfolio"
urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("projetos/<int:pk>/", views.detalhe, name="detalhe"),
]
