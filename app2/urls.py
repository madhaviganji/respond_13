from app2.views import *

from django.urls import path

app_name = 'life'

urlpatterns=[

    path('respond/',respond,name='respond'),

]



