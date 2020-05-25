from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('sending',views.sending, name='sending')
    ]