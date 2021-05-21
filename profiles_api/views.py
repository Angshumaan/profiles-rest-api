from django.shortcuts import render
from rest_framework.views import APIView
from  rest_framework.response import Response
from rest_framework import status

from . serializers import HelloSerializer
# Create your views here.

class HelloApiView(APIView):
    """Test API View get request from  user """
    serializer_class = HelloSerializer

    def get(self,request,format=None):
        an_apiview = [
        'uses HTTP methods as function (get,post,patch,put,delete)',
        'Is similar to a django taditional view',
        'Gives you the most control over the logic',
        'is manually mapped to URLS',
        ]

        '''Response converts it into json data..so it needs to be list or dictionary'''
        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self,request):
        """Create a hello mesasge with our name"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST,
            )

    def put(self,request,pk =None):
        """Handling updating an object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk =None):
        """Delte an object"""
        return Response({'method':'DELETE'})
