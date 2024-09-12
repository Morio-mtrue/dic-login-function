from django import forms


class TaskCreationForm(forms.Form):
    title = forms.CharField(label='titulo', max_length=255)
    content = forms.CharField(label='contenido', widget=forms.Textarea())
