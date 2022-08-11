from django.shortcuts import render
from .models import Noticia
from django.views import generic

# Create your views here.

class ListaNoticia(generic.ListView):
    model = Noticia
    
    def get_queryset(self):
        '''retorna las noticias ordenada por fecha publicada'''
        return Noticia.objects.order_by('-published_date')


class DetalleNoticia(generic.DetailView):
    model = Noticia


  
