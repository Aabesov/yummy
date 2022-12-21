from django.shortcuts import render
from django.views import generic


class IndexPageView(generic.TemplateView):
    template_name = "index.html"
    context_object_name = 'index'

