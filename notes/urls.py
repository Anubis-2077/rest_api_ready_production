from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from .views import *

#api versioning 
router = routers.DefaultRouter()
router.register(r'notes', NoteView, 'notes')
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path ("api/v1/", include(router.urls)),
    path('docs/', include_docs_urls(title="Notes API"))
]
