from django.shortcuts import get_object_or_404, render
from .models import Projeto

def inicio(request):
    return render(request, "portfolio/inicio.html", {"projetos": Projeto.objects.filter(publicado=True)})

def detalhe(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk, publicado=True)
    return render(request, "portfolio/detalhe.html", {"projeto": projeto})
