from django.shortcuts import render
from rest_framework.views import APIView
from  rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from . serializers import HelloSerializer,UserProfileSerializer
from . models import UserProfile
from . permissions import UpdateOwnProfile
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



class HelloViewSet(viewsets.ViewSet):
    serializer_class = HelloSerializer
    """Test API View set"""
    def list(self,request):
        """Return a hello message"""
        a_viewset =[
        'Uses actions (list,Create,update,delete,partialdelte)',
        'Automatically maps to URLS using Routers',
        'Provides more functionality with less code'

        ]
        return Response({'message':'Hello','a_viewset':a_viewset})



    def create(self,request):
        """Create a new hello message"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name =serializer.validated_data.get('name')
            message = f'hello {name}! '

            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status =status.HTTP_400_BAD_REQUEST
            )
    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})



class UserProfileViewset(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
