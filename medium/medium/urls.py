from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  include('core.urls'), name='index'),
    path('blogs/', include('blogs.urls'), name='blogs'),
    path('auth/', include('auth.urls'), name='auth'),
]
