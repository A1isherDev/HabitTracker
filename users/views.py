from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status,serializers,permissions
from .serializers import RegisterSerializer, UserSerializer, LoginSerializer
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken

# from users import serializers


# Create your views here.



User = get_user_model()


# class RegisterView(APIView):
#     def post(self, request):
#         serializer = RegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "User created!"}, status=201)
#         return Response(serializer.errors, status=400)
    
class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        tokens = {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }

        return Response(
            data={"msg": "User registered successfully", "tokens": tokens},
            status=status.HTTP_201_CREATED,
        )
    

# class LoginView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         user = authenticate(
#             username=serializer.validated_data["username"],
#             password=serializer.validated_data["password"]
#         )

#         if user is None:
#             return Response({"error": "Invalid credentials"}, status=400)

#         refresh = RefreshToken.for_user(user)

#         return Response({
#             "refresh": str(refresh),
#             "access": str(refresh.access_token),
#         })

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]  # login endpointni hammaga ruxsat berish

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=status.HTTP_200_OK)
    
# class LoginView(serializers.Serializer):
#     username = serializers.CharField(required=True)
#     password = serializers.CharField(required=True, write_only=True)

#     def validate(self, data):
#         user = authenticate(
#             username=data.get("username"),
#             password=data.get("password")
#         )

#         if not user:
#             raise serializers.ValidationError("Invalid username or password.")

#         if not user.is_active:
#             raise serializers.ValidationError("User is inactive.")

#         data["user"] = user
#         return data


# class ProfileView(RetrieveAPIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         serializer = UserSerializer(request.user)
#         return Response(serializer.data)

class ProfileView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user