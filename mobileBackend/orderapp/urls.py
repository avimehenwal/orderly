from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from orderapp import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from .views import UpdateOrders, UserOrders

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'order', views.OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('update-order/', UpdateOrders.as_view(), name='update_orders'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/order-history', UserOrders.as_view(), name='user_orders'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
