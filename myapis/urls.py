from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books.views import BookViewSet

router = DefaultRouter()
router.register(r'book', BookViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

