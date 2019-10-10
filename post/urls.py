from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

#알아야할 것 : rest framework는 라우터라는 개념을 통해 url을 결정하는구나

router = DefaultRouter() 
router.register('post',views.PostViewSet) #router객체의 register함수 (첫번째 인자 = url , 함수 )
urlpatterns = [
    path('',include(router.urls)),
    
]