from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import SignupView, LogoutView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='auth-signup'),
    path('login/', TokenObtainPairView.as_view(), name='auth-login'),
    path('logout/', LogoutView.as_view(), name='auth-logout'),
]