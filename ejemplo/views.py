from django.shortcuts import render
from .models import Noticia
from django.views import generic

# Create your views here.

'''def mi_vista(request):
    noticias = Noticia.objects.all().order_by('title')
    context = {'noticias':noticias}
    return render(request, 'noticia_list.html', context)'''
class ListaNoticia(generic.ListView):
    model = Noticia
    template_name: 'ejemplo.html'

    def get_queryset(self):
        '''retorna las ultimas 5 publicaciones'''
        return Noticia.objects.order_by('title')[:5]

class DetalleNoticia(generic.DetailView):
    model = Noticia
    template_name = 'detalleNoticia.html'

    def get_queryset(self):
        query = super(DetalleNoticia, self).get_queryset()
        return query
