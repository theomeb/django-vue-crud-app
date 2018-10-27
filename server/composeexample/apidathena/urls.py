from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('confidentiality/', views.ListConfidentialityView.as_view(), name="confidentiality-all"),
    path('init/', views.init, name='init')

]