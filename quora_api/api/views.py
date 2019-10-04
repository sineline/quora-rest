from quora_api.api.serializer import (
    UserListSerializer,
    UserCreateSerializer,
    QuestionSerializer,
    QuestionCreateSerializer,
    AnswerSerializer
)
from quora_api.api.permissions import (
    IsAuthor
)
from quora_api.models import (
    Question,
    Answer
)
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets
from rest_framework.authentication import (TokenAuthentication, SessionAuthentication)
from rest_framework.decorators import authentication_classes  
from rest_framework.response import Response
from rest_framework import status
import re
from django.http import HttpResponse

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAdminUser]

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [IsAdminUser]

class QuestionDetail(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
    def get_queryset(self):
        if 'url_title' in self.kwargs.keys():
            url_title = self.kwargs['url_title']
            self.lookup_field = 'url_title'
            return Question.objects.filter(url_title=url_title)
        
        return self.queryset
    

@authentication_classes((TokenAuthentication, SessionAuthentication))
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    id_author = Question.objects.values('author')
    serializer_class = QuestionSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return QuestionCreateSerializer

        return QuestionSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if self.request.user.id != instance.author.id:
            #return HttpResponse(status=401)
            return Response(
                "Only the author can delete the question.",
                status=status.HTTP_401_UNAUTHORIZED, content_type=401)

        self.perform_destroy(instance)
        return Response("Deleted successfully.", status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        url_title = serializer.validated_data['title']
        url_title = re.sub(r'[^\w\s]', '', url_title)
        url_title = url_title.strip().replace(" ", "-").lower()

        serializer.save(author=self.request.user, url_title=url_title)

    
class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

