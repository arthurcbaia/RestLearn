"""RestTutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Turismo.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracoesViewSet
from comments.api.viewsets import CommentsViewSet
from location.api.viewsets import LocationViewSet
from reviews.api.viewsets import ReviewsViewSet
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'PontoTuristico', PontoTuristicoViewSet, basename = 'PontoTuristico')
router.register(r'Atracoes', AtracoesViewSet)
router.register(r'Comments', CommentsViewSet)
router.register(r'Location', LocationViewSet)
router.register(r'Review', ReviewsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
