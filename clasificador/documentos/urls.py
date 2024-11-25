from django.urls import path, include
from .views import cargar_archivo, listar_documentos

urlpatterns = [
    path('cargar/', cargar_archivo, name='cargar_archivo'),
    path('listar/', listar_documentos, name='listar_documentos'),
    path('accounts/', include('django.contrib.auth.urls')),
]
