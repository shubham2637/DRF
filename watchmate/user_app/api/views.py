from rest_framework.decorators import api_view
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from user_app.api.serializers import RegistrationSerializer
# from user_app import models


from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@api_view( ['POST', ] )
def registration_view(request):
    if request.method == 'POST':
        data = dict()
        serializer = RegistrationSerializer( data=request.data )
        if serializer.is_valid():
            account = serializer.save()
            data['username'] = account.username
            data['email'] = account.email
            refresh = get_tokens_for_user(user=account)
            data['token'] = refresh
            data['res_str'] = "Registration Successful"
            return Response( data, status=HTTP_201_CREATED )
        data = serializer.errors
        return Response( data, status=HTTP_400_BAD_REQUEST )


@api_view( ['POST', ] )
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response( status=HTTP_200_OK )
