from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'ejemplo'
urlpatterns = [
    path('',views.Indice.as_view(), name='ejemploIndice'),
    path('',views.ListaNoticia.as_view(),name='ejemploNoticias'),
    path('<int:pk>',views.DetalleNoticia.as_view(), name='detalleUnaNoticia')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)