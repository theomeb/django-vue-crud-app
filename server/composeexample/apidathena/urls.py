from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('confidentiality/', views.ListConfidentialityView.as_view(), name="confidentiality-all"),
    path('language/', views.ListLanguageView.as_view(), name="language-all"),
    path('doctype/', views.ListDoctypeView.as_view(), name="doctype-all"),
    path('init/', views.init, name='init'),
    path('delete/', views.delete, name='delete'),
    path('create/', views.create, name="create"),
    path('edit/', views.edit, name="edit")
]