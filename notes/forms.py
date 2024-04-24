from  django import forms

from .models import Notes

class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        widgets  = {
            'title':forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={"class": 'form-countrol my-5'})
        }   
        labels = {
            'text': 'Write your thoughts here:'
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise forms.ValidationError('We only accept note about Django !')
        return title 
