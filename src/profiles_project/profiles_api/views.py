from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'User HTTP methods as functions',
            'It is simple',
            'Gives you the most control',
            'Is mapped manually'
        ]

        return Response({'message': 'Hello World!', 'an_apiview': an_apiview})
