from django.urls import path
from .views import upload_file
from . import views

urlpatterns = [
    path('', upload_file, name='upload_file'),
    path('download-sample/', views.download_sample, name='download_sample'),

]

