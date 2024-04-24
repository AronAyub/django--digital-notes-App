from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView

from .forms import NoteForm
from .models import Notes

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'note/notes_delete.html'

class NotesUpdateView(UpdateView):
    model = Notes
    success_url  = '/smart/notes'
    form_class = NoteForm
    
class NoteCreateView(CreateView):
    model = Notes
    success_url  = '/smart/notes'
    form_class = NoteForm
class NotesListView(ListView):
    model = Notes 
    context_object_name = "notes"
    template_name ="notes/notes.list.html"

class NotesDetailView(DetailView):
    model = Notes
    context_object_name =  "note"
    
#receive  a private key
def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exist")
    return render(request, 'notes/notes_detail.html', {'note': note})
