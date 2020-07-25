from django.shortcuts import render

from django.views.generic import FormView
from .forms import BlahForm

class BlahView(FormView):
    template_name = "index.html"
    form_class = BlahForm

    def post(self, request, *args, **kwargs):
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


blah = BlahView.as_view()