import secrets

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import EmailOTPChallenge
import hmac
import hashlib
from django.conf import settings
from datetime import timedelta
from django.utils import timezone


# Create your views here.
class CreateUserView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            otp = str(secrets.randbelow(1000000)).zfill(6)

           
            code_hash = hmac.new(
                settings.SECRET_KEY.encode(),
                otp.encode(),
                hashlib.sha256
                ).hexdigest()
            
            expires_at = timezone.now() + timedelta(minutes=10)
            
            EmailOTPChallenge.objects.create(
                user=user,
                code_hash = code_hash,
                expires_at=expires_at
            )
        
            return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        
    