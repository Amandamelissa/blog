from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']
        widgets = {
            'author': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Qual seu nome?'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-area',
                'placeholder': 'Escreva seu comentário aqui...'
            }),
        }