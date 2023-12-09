from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Note


def homecreate(request):
    
    context = {
        'status':request.GET.get('status'),
        'notas': get_list_or_404(Note)
    }
    
    if request.method == 'POST':
        body =  request.POST.get('body')
        print(len(body))
        if len(body) == 0:
            return redirect('/?status=0')
        else:
            note =  Note(body=body)
            note.save()
            return redirect('/?status=1')
    return render(request, 'homecreate.html', context)

def delete(request, id):
    nota = get_object_or_404(Note, id=id)
    nota.delete()
    

def updatenote(request, id):
    nota = get_object_or_404(Note, id=id)
    contexto = {
        'nota':nota,
    }
    if request.method == 'POST':
        try:
            Note.objects.filter(id=id).update(body=request.POST.get('body'))
            return redirect('/?status=2')
        except:
            print('ocorreu um erro na actualizacao do dado')
    
    
    return render(request, 'update.html', contexto)

def listall(request):
    notas = get_list_or_404(Note)
    contexto = {'notas':notas}
    return render(request, 'listall.html',contexto)

