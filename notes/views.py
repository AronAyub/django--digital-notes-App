from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NoteForm
from .models import Notes


class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'
    login_url = "/login"

class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NoteForm
    login_url = "/login"

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NoteForm
    login_url = "/login"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
        
class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    context_object_name = "note"
    login_url = "/login"










# from typing import Any
# from django.db.models.query import QuerySet
# from django.http.response import HttpResponseRedirect
# from django.forms import BaseModelForm
# from django.shortcuts import render
# from django.http import Http404, HttpResponse
# from django.views.generic import CreateView, DetailView, ListView, UpdateView
# from django.views.generic.edit import DeleteView
# from django.contrib.auth.mixins import  LoginRequiredMixin

# from .forms import NoteForm
# from .models import Notes

# class NotesDeleteView(DeleteView):
#     model = Notes
#     success_url = '/smart/notes'
#     template_name = 'notes/notes_delete.html'
   
# class NotesUpdateView(UpdateView):
#     model = Notes
#     success_url  = '/smart/notes'
#     form_class = NoteForm
    
# class NoteCreateView(LoginRequiredMixin, CreateView):
#     model = Notes
#     success_url  = '/smart/notes'
#     form_class = NoteForm
#     login_url = "/admin"


#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.user =  self.request.user
#         self.object.save()
#         return HttpResponse(self.get_success_url)
    


# class NotesListView(LoginRequiredMixin, ListView):
#     model = Notes 
#     context_object_name = "notes"
#     template_name ="notes/notes.list.html"
#     login_url = "/admin"

#     def get_queryset(self):
#         return self.request.user.notes.all()

# class NotesDetailView(DetailView):
#     model = Notes
#     context_object_name =  "note"
    
# #receive  a private key
# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note doesn't exist")
#     return render(request, 'notes/notes_detail.html', {'note': note})
