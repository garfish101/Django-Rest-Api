from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test Api View"""
    def get(self,request, format= None):
        """Returns a list of api features"""
        an_apiview = [
            'uses HTTP methods as functions (get,post,patch,put,delete)',
            'is similar to a tradisional django view',
            'gives you the most controle over your app logic',
            'is mapped manually to Urls',

        ]
        return Response({'message':'Hello!', 'an_apiview':an_apiview})
