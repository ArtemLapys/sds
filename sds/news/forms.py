from pyexpat import model
from django.core.exceptions import ValidationError
# from certifi import contents
from django import forms
from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content',
                  'image', 'published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

	#делаем валидацию для поля. формат: clean_названиеПоля
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 100:
        #   textError = 
          raise ValidationError(
              'Длина не должна превышать 100 символов! Ваш заголовок ' + str(len(title)) + ' символов.')

        return title

    def clean_content(self):
        title = self.cleaned_data['content']
        if len(title) < 70:
            #   textError =
          raise ValidationError(
              'Длина текста должна быть больше 70 символов! Ваш текст состоит из ' + str(len(title)) + ' символов.')
        return title



