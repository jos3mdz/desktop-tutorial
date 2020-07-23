from django.shortcuts import render, HttpResponse, redirect
from NotesD.forms import NewNote
from NotesD.models import modelNote


# Create your views here.
def home(request):
    lista=modelNote.objects.all().order_by('id').reverse()
    return render(request, "NotesD/index.html",{"lista":lista})

def create(request):
    if request.method=="POST":
        nota=NewNote(request.POST)
        if nota.is_valid():
            infNote=nota.cleaned_data
            ttl=infNote.get("Titulo")
            nte=infNote.get("Nota")
            SaveNote=modelNote(Title=ttl ,Note=nte)
            SaveNote.save()
    else:
        nos=NewNote()
    return render(request,"NotesD/create.html",{"Notes":NewNote})

def edit(request,id):
    inst= modelNote.objects.get(id=id)
    if request.method=="POST":
        nota=NewNote(request.POST)
        if nota.is_valid():
            infNote=nota.cleaned_data
            ttl=infNote.get("Titulo")
            nte=infNote.get("Nota")
            newEd= modelNote(id=id, Title=ttl, Note=nte)
            newEd.save()
    search=modelNote.objects.all().filter(id=id)
    return render(request, "NotesD/edit.html",{'nota':search})

def dele(request,id):
    idel=modelNote.objects.get(id=id)
    idel.delete()
    lista=modelNote.objects.all().order_by('id').reverse()
    return redirect('home')
