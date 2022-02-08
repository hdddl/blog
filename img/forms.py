from django import forms
from .models import Image, Album


class UploadImage(forms.ModelForm):
    album = forms.ModelChoiceField(queryset=Album.objects.all())

    class Meta:
        model = Image
        fields = ('name', 'album', 'image')
