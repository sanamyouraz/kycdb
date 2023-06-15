from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate

from .models import UserRegister
from .models import UserLogin

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserRegister.objects.all()
    serializer_class = UserSerializer





class LoginView(APIView):
    def post(self, request):
        username_email = request.data.get('username_email')
        password = request.data.get('password')

        user = authenticate(request, username=username_email, password=password)
        if user is not None:
            # Perform additional actions if needed
            return Response({'message': 'Login successful'})
        else:
            return Response({'message': 'Invalid username/email or password'}, status=400)

