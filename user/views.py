from rest_framework import permissions
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import CustomUserSerializer
from django.contrib.auth import get_user_model


# Create your views here.
class CustomUserRegisterView(generics.CreateAPIView):
    User = get_user_model()
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomUserSerializer


    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(status=status.HTTP_201_CREATED)