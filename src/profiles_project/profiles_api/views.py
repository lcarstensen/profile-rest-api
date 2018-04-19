from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers

class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'User HTTP methods as functions',
            'It is simple',
            'Gives you the most control',
            'Is mapped manually'
        ]

        return Response({'message': 'Hello World!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a Hello message with our name."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """ Handles updating an object"""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """ Patch request, only updates fields provided in the request"""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """ Deletes an object """

        return Response({'method': 'delete'})

class HelloViewSet(viewsets.ViewSet):
    """ Test API ViewSet"""

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'uses actions {list, create, retrieve, update, partial_update}',
            'automatically maps to URls using Routers',
            'provides more functionality with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})
