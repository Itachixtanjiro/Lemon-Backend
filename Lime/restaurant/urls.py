from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from restaurant.views import BookingViewSet 

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet),  # Register the UserViewSet
router.register(r'tables', BookingViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('menu-items/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),
    path('message/', views.msg, name='message'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'), # Include router-generated URLs
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # DRF browsable API login
]

