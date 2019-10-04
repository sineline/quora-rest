

from rest_framework.authtoken import views
#from snippets import views
from django.urls import path, include
from rest_framework import routers
from quora_api.api.views import (
    UserList,
    UserCreate,
    UserDetail,
    QuestionViewSet,
    QuestionDetail,
    AnswerViewSet
)

router = routers.DefaultRouter()
router.register('questions', QuestionViewSet)
router.register('answers', AnswerViewSet)

urlpatterns = [
    path('users/add/', UserCreate.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('token-auth/', views.obtain_auth_token),
    path('questions-title/<slug:url_title>/', QuestionDetail.as_view()),
] 

urlpatterns += router.urls
