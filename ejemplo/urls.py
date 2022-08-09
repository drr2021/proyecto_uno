from django.urls import path
from . import views

app_name = 'ejemplo'
urlpatterns = [
    path('lista',views.ListaNoticia.as_view()),
    path('detalle/<int:pk>',views.DetalleNoticia.as_view())
]