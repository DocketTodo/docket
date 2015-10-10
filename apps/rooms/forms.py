from django import forms

from .models import Room

class RoomCreateForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ['name', 'description', 'user' ]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(RoomCreateForm, self).__init__(*args, **kwargs)
        self.fields['user'].initial = self.user