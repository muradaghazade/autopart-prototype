from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('magazine-list/', magazine_list, name='magazine-list'),
]