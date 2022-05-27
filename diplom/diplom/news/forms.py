from django.forms import ModelForm, DateTimeInput, Textarea
from apinews.models import ApiNews, Comment
from django.forms.widgets import TextInput, FileInput, Textarea

class NewsForm(ModelForm):
    class Meta:
        model = ApiNews
        fields = ['title','description', 'text', 'image']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            'description': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ввдите описание'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст'
            }),    
            'image': FileInput(attrs={
                'class': 'form-control',
            }),    
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

        widgets = {
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
        }