from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from .serializers import UserSerializer, ChatHistorySerializer
from .models import ChatHistory
from .utils import get_chatbot_response

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        return Response({
            'message': 'Login successful',
            'user_id': user.id,
            'username': user.username
        })
    return Response(
        {'error': 'Invalid credentials'},
        status=status.HTTP_401_UNAUTHORIZED
    )

@api_view(['POST'])
def chat(request):
    try:
        message = request.data.get('message')
        language = request.data.get('language', 'en')
        user_id = request.data.get('user_id') 

        if not message:
            return Response(
                {'error': 'Message is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

       
        response = get_chatbot_response(message, language)

        if user_id:
            try:
                from django.contrib.auth.models import User
                user = User.objects.get(id=user_id)
                chat_history = ChatHistory.objects.create(
                    user=user,
                    message=message,
                    response=response,
                    language=language
                )
                serializer = ChatHistorySerializer(chat_history)
                return Response(serializer.data)
            except User.DoesNotExist:
                pass

        return Response({
            'message': message,
            'response': response,
            'language': language
        })
    
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['GET'])
def chat_history(request):
    user_id = request.query_params.get('user_id')
    if user_id:
        try:
            from django.contrib.auth.models import User
            user = User.objects.get(id=user_id)
            history = ChatHistory.objects.filter(user=user)
            serializer = ChatHistorySerializer(history, many=True)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response([])
    return Response([])