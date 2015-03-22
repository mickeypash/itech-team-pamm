from django import forms
from django.contrib.auth.models import User
from backup.models import Note,Folder,Tag, UserProfile

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content', 'tag')

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ('title', 'note')

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('label',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')