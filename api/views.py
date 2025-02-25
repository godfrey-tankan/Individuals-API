from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import Individual, CustomUser
from .serializers import IndividualSerializer, CustomUserSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

class IndividualListCreateView(generics.ListCreateAPIView):
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class IndividualDetailView(generics.RetrieveAPIView):
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        data["api_key"] = user.api_key
        return data

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

