from ckeditor.widgets import CKEditorWidget
from django import forms
from django_select2.forms import Select2Widget
from suit.widgets import EnclosedInput

from .models import Events


class EventsForm(forms.ModelForm):

    class Meta:
        model = Events
        fields = (
            'title',
            'dateStart',
            'dateEnd',
        )

        widgets = {
            'title': EnclosedInput(prepend='№', append='fa-home', attrs={'placeholder': 'квартира'}),
        }
