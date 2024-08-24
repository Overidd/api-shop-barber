from rest_framework.generics import (
   ListAPIView,
   CreateAPIView,
   UpdateAPIView,
   DestroyAPIView,
)
from rest_framework import status
from rest_framework.response import Response 
from django.http import Http404
from .serializers import RoleSerializer, UserSerializer, LoginSerializer
from .models import MyUserModel, RoleModel
from rest_framework.exceptions import NotFound
from rest_framework.serializers import ValidationError

# Create your views here.


class RoleListViews(ListAPIView):
   queryset = RoleModel.objects.all()
   serializer_class = RoleSerializer
   
   def list(self, request, *args, **kwargs):
      response  = super().list(request, *args, **kwargs)
      return Response({
         'message': 'List fetched successfully',
         'data': response.data
      },status=status.HTTP_200_OK)
   

class RoleCreateViews(CreateAPIView):
   queryset = RoleModel.objects.all()
   serializer_class = RoleSerializer

   def create(self, request, *args, **kwargs):
      response = super().create(request, *args, **kwargs)
      return Response({
         'message': 'Role created successfully',
         'data': response.data
      },status=status.HTTP_201_CREATED)
      
class RoleUpdateView(UpdateAPIView):
   queryset = RoleModel.objects.all()
   serializer_class = RoleSerializer

   def update(self, request, *args, **kwargs):
      try:

         response = super().update(request, *args, **kwargs)
         return Response({
            'message': 'Role updated successfully',
            'data': response.data
         },status=status.HTTP_200_OK)
      except Http404:
         return Response({
            'message': 'Role not found',
         }, status=status.HTTP_404_NOT_FOUND)

class RoleDestroyView(DestroyAPIView):
   queryset = RoleModel.objects.all()
   serializer_class = RoleSerializer
   
   def destroy(self, request, *args, **kwargs):
      response = super().destroy(request, *args, **kwargs)
      try: 
         return Response({
            'message': 'Role deleted successfully',
            'data': response.data
         }, status=status.HTTP_200_OK)
      except Http404:
         return Response({
               'message': 'Role not found',
            }, status=status.HTTP_404_NOT_FOUND)   

#*------------------

class UserListViews(ListAPIView):
   queryset = MyUserModel.objects.all()
   serializer_class = UserSerializer
   
   def list(self, request, *args, **kwargs):
      response = super().list(request, *args, **kwargs)
      return Response({
         'message': 'List fetched successfully',
         'data': response.data
      },status=status.HTTP_200_OK)
   

class UserCreateView(CreateAPIView):
   serializer_class = UserSerializer
   
   def create(self, request, *args, **kwargs):
      response = super().create(request, *args, **kwargs)

      return Response({
         'message': 'User created successfully',
         'data': response.data
      },status=status.HTTP_201_CREATED)
   

class UserUpdateView(UpdateAPIView):
   queryset = MyUserModel.objects.all()
   serializer_class = UserSerializer

   def update(self, request, *args, **kwargs):
      response = super().update(request, *args, **kwargs)

      try:
            return Response({
               'message': 'User updated successfully',
               'data': response.data
         },status=status.HTTP_200_OK)  
      except Http404:
         return Response({
            'message': 'User not found',
         }, status=status.HTTP_404_NOT_FOUND)

class UserDestroyView(DestroyAPIView):
   queryset = MyUserModel.objects.all()
   serializer_class = UserSerializer

   def destroy(self, request, *args, **kwargs):
      try:
         instance = self.get_object()
         instance.status = False
         instance.save()

         serializer = self.get_serializer(instance)
         return Response({
            'message': 'User deleted successfully',
            'data': serializer.data
         }, status=status.HTTP_200_OK)
      except Http404:
         return Response({
            'message': 'User not found',
         }, status=status.HTTP_404_NOT_FOUND)
      
#*------------------
from rest_framework_simplejwt.views import (
   TokenObtainPairView,
   TokenRefreshView,
)
class LoginView(TokenObtainPairView):
   serializer_class = LoginSerializer

   def post(self, request, *args, **kw):
      try:
         return super().post(request, *args, **kw)
      except ValidationError as e:
         return Response({
            'message': 'User account is disabled',
         }, status=status.HTTP_400_BAD_REQUEST)