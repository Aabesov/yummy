from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPageView.as_view(), name="index"),
    path("update/<int:pk>/", views.edit, name="update_food"),
    path("delete/<int:pk>/", views.delete),
    # path('inner/', views.InnerPageView.as_view(), name="inner"),
    path("create/", views.create),
]