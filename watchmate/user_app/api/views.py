from rest_framework.decorators import api_view
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from user_app.api.serializers import RegistrationSerializer
from user_app import models


@api_view(['POST',])
def registration_view(request):

    if request.method == 'POST':
        data = dict()
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            data['username'] = account.username
            data['email'] = account.email

            token = Token.objects.get(user_id=account.pk).key
            data['token'] = token
            data['res_str'] = "Registration Successful"
            return Response(data, status=HTTP_201_CREATED)
        data = serializer.errors
        return Response(data ,status=HTTP_400_BAD_REQUEST)
