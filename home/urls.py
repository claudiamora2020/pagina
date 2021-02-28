from django.urls import path
from .views import vista_about
from .views import vista_contact

urlpatterns = [

    path('about/', vista_about),
    path('contact/', vista_contact),
]