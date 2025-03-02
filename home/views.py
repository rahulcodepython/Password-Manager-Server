from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from . import serializers, models

# Create your views here.

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})

        return Response({'error': 'Invalid Credentials'}, status=400)


class RecordView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        passwords = models.Password.objects.all()
        serialized = serializers.PasswordSerializer(passwords, many=True)
        return Response(serialized.data)

    def post(self, request):
        serialized = serializers.PasswordSerializer(data=request.data)

        if serialized.is_valid():
            serialized.save()
            return Response({'success': True}, status=201)

        return Response(serialized.errors, status=400)

    def patch(self, request):
        password = models.Password.objects.get(id=request.data.get('id'))
        serialized = serializers.PasswordSerializer(password, data=request.data, partial=True)

        if serialized.is_valid():
            serialized.save()
            return Response({'success': True}, status=201)

        return Response(serialized.errors, status=400)

    def delete(self, request):
        password = get_object_or_404(models.Password, id=request.data.get('id'))

        if password:
            password.delete()
            return Response({'success': True}, status=201)

        return Response({'error': 'Invalid Credentials'}, status=400)