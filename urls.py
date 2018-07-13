from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('input', views.input, name='input'),
    path('output', views.output, name='output')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)