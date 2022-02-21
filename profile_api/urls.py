from django import urls
from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views

router = DefaultRouter()
router.register("hello-viewset", views.HelloViewSet, base_name="hello-viewset")
urlpatterns=[

    path('hello-view/', views.HelloApiView.as_view()),
    path("",include(router.urls))

    ]