from django.contrib import admin
from django.urls import path, include
from prometheus_client import multiprocess, generate_latest, CollectorRegistry, CONTENT_TYPE_LATEST
from django.http import HttpResponse


def metrics(request):
    registry = CollectorRegistry()
    multiprocess.MultiProcessCollector(registry)
    data = generate_latest(registry)
    return HttpResponse(data, content_type=CONTENT_TYPE_LATEST)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  include('core.urls'), name='index'),
    path('blogs/', include('blogs.urls'), name='blogs'),
    path('auth/', include('auth.urls'), name='auth'),
    path('metrics/', metrics, name='prometheus-metrics'),
]
