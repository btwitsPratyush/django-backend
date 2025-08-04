from django.utils import timezone
from django.contrib.auth import get_user_model

from rest_framework import viewsets, status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Payout
from .serializers import UserSerializer, PayoutSerializer, HealthCheckSerializer

User = get_user_model()

# ==========================
# User Registration View
# ==========================
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

# ==========================
# User ViewSet (for router)
# ==========================
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# ==========================
# Payout ViewSet
# ==========================
class PayoutViewSet(viewsets.ModelViewSet):
    queryset = Payout.objects.all().order_by('-created_at')
    serializer_class = PayoutSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ==========================
# Health Check Endpoint
# ==========================
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


# ==========================
# API Info Endpoint
# ==========================
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
            'protected': '/api/auth/protected/',
            'admin': '/admin/',
        }
    }, status=status.HTTP_200_OK)


# ==========================
# JWT Protected Test Endpoint
# ==========================
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_data(request):
    """
    Protected endpoint to test JWT authentication
    """
    return Response({
        'message': f'Hello, {request.user.username}! You are authenticated.',
        'user_id': request.user.id,
        'email': request.user.email,
    }, status=status.HTTP_200_OK)