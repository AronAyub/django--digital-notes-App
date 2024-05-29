from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('smart/', include('notes.urls')),
    path('thanks/', TemplateView.as_view(template_name='home/thanks.html'), name='thanks'),
]
