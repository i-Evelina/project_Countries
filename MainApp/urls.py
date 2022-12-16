from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('countries_list', views.countries_list),
    path('countries_list/<int:country_id>/', views.countries_detail),
    path('countries_list/alphabet/<int:alphabet_id>/', views.alphabet_search),
    path('languages', views.languages),
    path('languages/<int:languages_id>/', views.languages_country),
]