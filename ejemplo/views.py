from django.shortcuts import render

# Create your views here.

#from django.http import HttpResponse
#def mi_vista(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def mi_vista(request):
    return render(request, 'ejemplo/post_list.html', {})
