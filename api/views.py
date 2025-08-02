from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.utils import timezone

from .models import Payout
from .serializers import UserSerializer, HealthCheckSerializer, PayoutSerializer


# User ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Health check endpoint
@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    """
    Simple health check endpoint to verify the API is running
    """
    data = {
        'status': 'healthy',
        'message': 'Payment Gateway API is running successfully!',
        'timestamp': timezone.now()
    }
    serializer = HealthCheckSerializer(data)
    return Response(serializer.data, status=status.HTTP_200_OK)


# API Info endpoint
@api_view(['GET'])
@permission_classes([AllowAny])
def api_info(request):
    """
    API information endpoint
    """
    return Response({
        'name': 'Payment Gateway API',
        'version': '1.0.0',
        'description': 'Django REST Framework API for payment processing',
        'endpoints': {
            'health': '/api/health/',
            'info': '/api/info/',
            'users': '/api/users/',
            'payouts': '/api/payouts/',
            'admin': '/admin/',
        }
    }, status=status.HTTP_200_OK)


#  Payout ViewSet
class PayoutViewSet(viewsets.ModelViewSet):
    queryset = Payout.objects.all().order_by('-created_at')
    serializer_class = PayoutSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]