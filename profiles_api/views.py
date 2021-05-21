from django.shortcuts import render
from rest_framework.views import APIView
from  rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    """Test API View get request from  user """
    def get(self,request,format=None):
        an_apiview = [
        'uses HTTP methods as function (get,post,patch,put,delete)',
        'Is similar to a django taditional view',
        'Gives you the most control over the logic',
        'is manually mapped to URLS',
        ]

        '''Response converts it into json data..so it needs to be list or dictionary'''
        return Response({'message':'Hello!','an_apiview':an_apiview})
