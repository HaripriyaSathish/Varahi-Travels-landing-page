from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('enquiry/submit/', views.submit_enquiry, name='submit_enquiry'),
]