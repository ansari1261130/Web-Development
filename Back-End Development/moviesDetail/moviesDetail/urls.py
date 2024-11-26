from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from movieSite.views import MovieViewSet, ActionViewSet,ComedyViewSet,AnimeViewSet,ScienceFictionViewSet

router = routers.SimpleRouter()
router.register('movies', MovieViewSet, basename='movie') 
router.register('actions', ActionViewSet, basename='action') 
router.register('comedy', ComedyViewSet, basename='comedy') 
router.register('anime', AnimeViewSet, basename='anime') 
router.register('science_fiction', ScienceFictionViewSet, basename='science_fiction') 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] + static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)