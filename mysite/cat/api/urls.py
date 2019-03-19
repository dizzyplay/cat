from django.urls import path
from . import views

app_name = 'cat'

urlpatterns = [
    path('cat/', views.main, name="main")
]
