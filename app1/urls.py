from app1.views import *

from django.urls import path

app_name = 'iam'

urlpatterns=[
    path('yashwanth/',yashwanth,name='yashwanth'),
]

