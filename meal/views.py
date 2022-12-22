from django.shortcuts import render
from django.views import generic

from meal.models import Food


class IndexPageView(generic.ListView):
    # model = Meal
    template_name = "index.html"
    context_object_name = 'index'

    def get_queryset(self):
        queryset = Food.objects.all()
        return queryset


# class InnerPageView(generic.TemplateView):
#     template_name = "sample-inner-page.html"
#     context_object_name = 'inner'