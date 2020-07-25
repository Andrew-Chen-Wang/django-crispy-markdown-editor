from django import forms

from .models import Blah

class MDWidget(forms.Textarea):
    template_name = "custom.html"

class BlahForm(forms.ModelForm):
    class Meta:
        model = Blah
        fields = "__all__"
        widgets = {
            "hi": MDWidget()
        }
