from api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'efo-terms', views.EfoTermViewSet)
router.register(r'efo-term-synonyms', views.EfoTermSynonymViewSet)
router.register(r'efo-term-ontology', views.EfoTermOntologyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('load-efo-terms/', views.LoadEfoTermsView.as_view(), name='load-efo-terms'),
]
