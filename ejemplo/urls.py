from django.urls import path
from . import views

app_name = 'ejemplo'
urlpatterns = [
    path('noticias',views.ListaNoticia.as_view()),
    path('noticias/<int:pk>',views.DetalleNoticia.as_view())
]