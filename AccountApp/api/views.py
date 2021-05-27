from rest_framework import status
from  rest_framework.response import  Response
from rest_framework.decorators import  api_view
from AccountApp.api.serializers import RegistrationSerializer,UserAccountSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated

@api_view(['POST',])
def registration_view(request):
    if request.method=='POST':
        serializer=RegistrationSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']="successfully added data"
            data['email']=account.email
            data['username']=account.username
            token = Token.objects.get(user=account).key
            data['token']=token

        else:
            data=serializer.errors
        return Response(data)


@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def userapiview(request):
    try:
        acccount=request.user
    except account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        serializer=UserAccountSerializer(acccount)
        return Response(serializer.data)
            
         
    
    