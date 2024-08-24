from django.urls import path
from .views import RoleListViews, RoleCreateViews, RoleUpdateView, RoleDestroyView, UserListViews, UserCreateView, UserUpdateView, UserDestroyView,LoginView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
   path('role/list/', RoleListViews.as_view()),
   path('role/create/', RoleCreateViews.as_view()),
   path('role/update/<int:pk>/', RoleUpdateView.as_view()),
   path('role/delete/<int:pk>/', RoleDestroyView.as_view()),
   
   path('user/list/', UserListViews.as_view()),
   path('user/create/', UserCreateView.as_view()),
   path('user/update/<int:pk>/', UserUpdateView.as_view()),
   path('user/delete/<int:pk>/', UserDestroyView.as_view()),

   path('login/', LoginView.as_view()),
   # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]