from django.urls import path
from . import views

urlpatterns = [
        path ('', views.index, name='index'),
        path ('submit/', views.submit, name='submit'),
        path ('thankyou/', views.thankyou, name='thankyou'),
        path ('start/', views.start, name='start'),
    ]
