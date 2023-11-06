from django.http import request
from django.urls import path

from catalog.views import home_page, contact_info

urlpatterns = [
    path('', home_page),
    path('', contact_info)
]
