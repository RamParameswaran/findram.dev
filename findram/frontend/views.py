from django.shortcuts import render
from django.views.generic import TemplateView

from .models import HomePage

# Create your views here.


class ContactPageView(TemplateView):
    template_name = "pages/contact.html"
