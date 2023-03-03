from django.contrib import admin
from django.urls import path
from Asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='uy'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('maqola/<int:son>/', maqola, name='maqola'),
]
