from django.urls import path
from app.views import addFile, allFiles

urlpatterns = [
    path('', addFile, name='add_file'),
    path('all_files', allFiles, name="all_files"),
]
