from django.forms import ModelForm
from notes.models import Note,Folder,Tag

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content', 'tag')


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ('label')
