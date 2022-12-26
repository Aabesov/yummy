from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Food
from meal.models import Food
from django.http import HttpResponseRedirect, HttpResponseNotFound


class IndexPageView(generic.ListView):
    template_name = "index.html"
    context_object_name = 'index'

    def get_queryset(self):
        queryset = Food.objects.all()
        return queryset


def create(request):
    if request.method == "POST":
        person = Food()
        person.name = request.POST.get("name")
        person.ingredients = request.POST.get("ingredients")
        person.picture = request.POST.get("picture")
        person.price = request.POST.get("price")
        person.category = request.POST.get("category")
        person.save()
    return HttpResponseRedirect("/")


def edit(request, pk):
    try:
        person = Food.objects.get(id=pk)

        if request.method == "POST":
            person.name = request.POST.get("name")
            person.ingredients = request.POST.get("ingredients")
            person.picture = request.POST.get("picture")
            person.price = request.POST.get("price")
            person.category = request.POST.get("category")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "update_food.html", {"person": person})
    except Food.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def delete(request, pk):
    try:
        person = Food.objects.get(id=pk)
        person.delete()
        return HttpResponseRedirect("/")
    except Food.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
