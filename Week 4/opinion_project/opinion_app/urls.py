from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-opinion/', views.add_opinion, name='add_opinion'),
    path('all-opinions/', views.all_opinions, name='all_opinions'),
    path('thank-you/', views.thank_you, name='thank_you'),

]
