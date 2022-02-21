
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

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



