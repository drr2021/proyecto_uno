from django.shortcuts import render
from .models import Noticia
from django.views import generic

# Create your views here.

class ListaNoticia(generic.ListView):
    model = Noticia
    template_name: 'noticia_list.html'

    def get_queryset(self):
        '''retorna las ultimas 5 publicaciones'''
        return Noticia.objects.order_by('title')


class DetalleNoticia(generic.DetailView):
    model = Noticia
    template_name: 'noticia_detail.html'

    def get_queryset(self):
        query = super(DetalleNoticia, self).get_queryset()
        return query
