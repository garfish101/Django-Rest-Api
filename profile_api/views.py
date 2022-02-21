
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from profile_api import models
from rest_framework.authentication import TokenAuthentication
from profile_api import permissions

class HelloApiView(APIView):
    """Test Api View"""
    serializer_class = serializers.hello_serializer

    def get(self,request, format= None):
        """Returns a list of api features"""
        an_apiview = [
            'uses HTTP methods as functions (get,post,patch,put,delete)',
            'is similar to a tradisional django view',
            'gives you the most controle over your app logic',
            'is mapped manually to Urls',

        ]
        return Response({'message':'Hello!', 'an_apiview':an_apiview})
    def post(self,request):
        """Create a hello massage with our name"""
        serializer= self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"hello {name}"
            return Response({"message": message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST 
                )

    def put(self,request, pk=None):
        """Handles updating an objects"""
        return Response({"method":"Put"})

    def patch(self,request , pk =None):
        """Returns a partial update of na object"""
        return Response({"method":"Patch"})

    def delete(self,request,pk=None):
        """delets and objects"""
        return Response({"method":"Delete"})


class HelloViewSet(viewsets.ViewSet):
    """Test API viewset"""
    serializer_class= serializers.hello_serializer

    def list(self,request):
        """returns a hello message"""
        a_viewset =[
            "Uses (List,create,retrive,update,partial_update,destroy)",
            "Automatically maps to urls using Routers",
            "Provides more functionallity with less code",
        ]
        return Response({"message":"hello", "a_viewset": a_viewset})

    def create(self,request):
        """Create a new hello message"""
        serialzer = self.serializer_class(data=request.data)

        if serialzer.is_valid():
            name = serialzer.validated_data.get("name")
            message = f"hello {name}"
            return Response({'message':message})
        else:
            return Response(
                serialzer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrive(self,request, pk=None):
        """Handles getting an objects by its id"""
        return Response({"http_method":"GET"})

    def update(self,request,pk=None):
        """Handles updating of an objects"""
        return Response({"http_method": "PUT"})

    def partial_update(self, request,pk=None):
        """Handles partially updating an objects """
        return Response({"http_method":"PATCH"})

    def destroy(self,request,pk=None):
        """Delete's a objects by its Id"""
        return Response({"http_method":"DELETE"})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating user profiles"""
    serializer_class = serializers.UserProfileSerialiser
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    

    


    
