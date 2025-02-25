from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, IndividualListCreateView, IndividualDetailView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("individuals/", IndividualListCreateView.as_view(), name="individual-list"),
    path("individuals/<int:pk>/", IndividualDetailView.as_view(), name="individual-detail"),
]
