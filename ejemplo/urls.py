from django.urls import path
from . import views


app_name = 'ejemplo'
urlpatterns = [
    path('',views.ListaNoticia.as_view(),name='ejemploNoticias'),
    path('<int:pk>',views.DetalleNoticia.as_view(), name='detalleUnaNoticia')
]