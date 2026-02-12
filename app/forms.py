from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

from .models import Piece
class PieceForm(forms.ModelForm):
    class Meta:
        model = Piece
        fields = ['collection', 'title', 'artist', 'artist_photo', 'type', 'year', 'piececover']
        widgets = {
             'collection': forms.Select(attrs={'class': 'form-control'}),
             'title': forms.TextInput(attrs={'class': 'form-control'}),
             'artist': forms.TextInput(attrs={'class': 'form-control'}),
             'artist_photo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Paste Artist Photo URL here'}),
             'type': forms.TextInput(attrs={'class': 'form-control'}),
             'year': forms.NumberInput(attrs={'class': 'form-control'}),
             'piececover': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Paste Image URL here'}),
        }
