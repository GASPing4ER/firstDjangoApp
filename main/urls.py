from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path("<int:id>", views.index, name="index"),
path("", views.home, name="home"),
path("home/", views.home, name="home"),
path("create/", views.create, name="create"),
path("view/", views.view, name="view"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)