from django import forms
from .models import  *

class frmBlog(forms.ModelForm):
    class Meta:
        model = Postagem

    def __init__(self, *args, **kwargs):
        super(frmBlog, self).__init__(*args, **kwargs)
        self.fields['autor'].error_messages['required'] = 'Autor esta vazio.'
        self.fields['titulo'].error_messages['required'] = 'Titulo esta vazio.'
        self.fields['titulo'].error_messages['max_length'] = 'Titulo esta com mais de 50 caracteres.'
        self.fields['briefing'].error_messages['required'] = 'Briefing esta vazio.'
        self.fields['briefing'].error_messages['max_length'] = 'Briefing esta com mais de 50 caracteres.'
        self.fields['texto'].error_messages['required'] = 'Texto esta vazio.'
        self.fields['texto'].error_messages['max_length'] = 'Titulo esta com mais de 1400 caracteres.'
        self.fields['dataCriacao'].error_messages['required'] = 'Data de criacao vazia.'
        self.fields['imagem'].error_messages['required'] = 'Image esta vazia.'
        self.fields['dataCriacao'].widget.attrs['readonly'] = True