from django.urls import path
from rest_framework.routers import DefaultRouter
from todo import views

router = DefaultRouter()

router.register('', views.TaskAPIView, 'api_tasks')

urlpatterns = router.urls