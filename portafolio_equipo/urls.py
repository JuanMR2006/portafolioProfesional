from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('juan/', include('cv_juan.urls')),
    path('miguel/', include('cv_miguel.urls')),
    path('sebas/', include('cv_sebas.urls')),
]