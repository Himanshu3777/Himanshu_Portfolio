
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls'))
    path('messages/', include('your_app.urls')),
]
