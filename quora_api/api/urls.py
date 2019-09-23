

from rest_framework.authtoken import views
#from snippets import views
from django.urls import path#, include
from rest_framework import routers
from quora_api.api.views import (UserList,
                                 UserCreate,
                                 UserDetail)

# Create a router and register our viewsets with it.
#router = routers.DefaultRouter()
#router.register(r'snippets', views.SnippetViewSet)
#router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('users/add/', UserCreate.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('token-auth/', views.obtain_auth_token)
#     #url(r'^api-token-auth/', views.obtain_auth_token)
]

