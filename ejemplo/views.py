from .models import Noticia
from django.views import generic

# Create your views here.

class ListaNoticia(generic.ListView):
    model = Noticia
    paginate_by = 10
    
    def get_queryset(self):
        '''retorna las noticias ordenada por fecha publicada'''
        return Noticia.objects.order_by('-published_date')


class DetalleNoticia(generic.DetailView):
    model = Noticia
    


  
