from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # 1. Importas RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/clinic/patients/')),  # 2. Rediriges la raíz
    path('admin/', admin.site.urls),
    path('veterinary/', include('veterinary.urls')),
    path('clinic/', include('clinic.urls')),
]