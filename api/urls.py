from django import views
from django.urls import path,include
from api.views import MyObtainTokenPairView,RegisterView,InventoryView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'inventory',InventoryView, basename='inventory')



urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('',include(router.urls)),
]