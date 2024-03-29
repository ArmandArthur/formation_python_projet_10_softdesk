from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib import auth


class RegisterView(GenericAPIView):
    '''
        Register View API
    '''
    serializer_class = RegisterSerializer

    def post(self, request):
        '''
            The name about method is post
            @Return Reponse with data user
        '''
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    '''
        Login View API
    '''
    serializer_class = LoginSerializer

    def post(self, request):
        '''
            The name about method is post
            @Return Response with token
        '''
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user = auth.authenticate(email=data["email"], password=data["password"])

        # Generate Token
        refresh = RefreshToken.for_user(user)

        return Response(
            {"access": str(refresh.access_token), "refresh": str(refresh)},
            status=status.HTTP_200_OK,
        )
