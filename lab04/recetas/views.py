from django.shortcuts import render

# Create your views here.
from .models import Receta, Autor, Comentario

# Create your views here.
def index(request):
    latest_question_list = Receta.objects.all()
    context = {
        'latest_question_list':latest_question_list
    }
    return render(request,'recetas/index.html',context)

