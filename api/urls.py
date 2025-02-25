from django.urls import path
from .views import (
    CustomTokenObtainPairView,
    IndividualRetrieveView,
)

urlpatterns = [
    path("login/", CustomTokenObtainPairView.as_view(), name="login"),
    path("individual/", IndividualRetrieveView.as_view(), name="individual-detail"),
]