from django.urls import path
from .views import home

app_name = 'courses'
urlpatterns = [
    path('' , home ,name='mtaa'),
]
