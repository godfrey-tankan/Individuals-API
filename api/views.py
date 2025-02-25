from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import Individual, CustomUser
from .serializers import IndividualSerializer, CustomUserSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import NotFound,PermissionDenied
from django.utils.timezone import now
from datetime import timedelta

class IndividualRetrieveView(generics.RetrieveAPIView):
    serializer_class = IndividualSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user

        if not user.is_premium:
            if user.last_request_time:
                time_since_last_request = now() - user.last_request_time
                if time_since_last_request < timedelta(minutes=2):
                    raise PermissionDenied("You must wait at least 2 minutes between requests.")
        
        if not user.is_premium:
            if user.credits <= 0:
                raise PermissionDenied("You have run out of credits. Upgrade to premium for unlimited access.")
        
        national_id = self.request.query_params.get("national_id")
        phone_number = self.request.query_params.get("phone_number")

        if not national_id and not phone_number:
            raise NotFound("Provide a National ID or Phone Number")

        try:
            if national_id:
                individual = Individual.objects.get(national_id=national_id)
            elif phone_number:
                individual = Individual.objects.get(phone_number=phone_number)
            
            if not user.is_premium:
                user.credits -= 1
                user.last_request_time = now()
                user.save()

            return individual

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

