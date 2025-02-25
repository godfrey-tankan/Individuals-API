from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import Individual, CustomUser
from .serializers import IndividualSerializer, CustomUserSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import NotFound

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

class IndividualRetrieveView(generics.RetrieveAPIView):
    serializer_class = IndividualSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        national_id = self.request.query_params.get("national_id")
        phone_number = self.request.query_params.get("phone_number")

        if not national_id and not phone_number:
            raise NotFound("Provide a National ID or Phone Number")

        try:
            if national_id:
                return Individual.objects.get(national_id=national_id)
            if phone_number:
                return Individual.objects.get(phone_number=phone_number)
        except Individual.DoesNotExist:
            raise NotFound("No Individual found with the given details")

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        data["api_key"] = user.api_key
        return data

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

