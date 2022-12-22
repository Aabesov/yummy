from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPageView.as_view(), name="index"),
    # path('inner/', views.InnerPageView.as_view(), name="inner"),

]