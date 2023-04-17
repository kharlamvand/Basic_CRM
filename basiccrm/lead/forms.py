from django import forms

from .models import Lead, Comment, LeadFile


class AddLeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ('name', 'email', 'description', 'priority', 'status',)

    name = forms.CharField(label="", widget=forms.TextInput(attrs={
        'placeholder': 'Название',
        'class': 'bg-form'
    }))

    email = forms.CharField(label="", widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'bg-form'
    }))

    description = forms.CharField(label="", widget=forms.TextInput(attrs={
        'placeholder': 'Описание',
        'class': 'bg-form'
    }))


class AddCommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.TextInput(attrs={
        'placeholder': 'Добавить информацию',
        'class': 'bg-comment1'
    }))

    class Meta:
        model = Comment
        fields = ('content',)


class AddFileForm(forms.ModelForm):
    class Meta:
        model = LeadFile
        fields = ('file',)
