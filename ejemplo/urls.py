from django.urls import path
from . import views

urlpatterns = [
    path('',views.ListaNoticia.as_view(), name='lasNoticias'),
    path('<int:pk>',views.DetalleNoticia.as_view(), name='unaNoticia')
]