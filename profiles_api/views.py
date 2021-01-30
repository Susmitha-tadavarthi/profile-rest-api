from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

from rest_framework import viewsets

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIViews Features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, put, patch, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over the your application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})

    def post(self, request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating a object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handling partial updates on objects"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """delete an object"""
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Testing API Viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Retuen a hello message"""

        a_viewset = [
            'Uses actions (list, create, retrive, update, partial_update)',
            'Automatically maps to URLs using routers',
            'provides more functioanality with less code',
        ]

        return Response({'Message':'Hello!','a_viewset':a_viewset})

    def create(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message = f'hello {name}!'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'HTTP method':'GET'})

    def update(self, request, pk=None):
        """Handle updating of an object"""
        return Response({'HTTP method' : 'PUT'})

    def partial_update(self, request, pk=None):
        """Handling updating part of an object"""
        return Response({'HTTP method' : 'PATCH'})

    def destroy(self, request, pk=None):
        """Handling removing an object"""
        return Response({'HTTP Method' : 'DELETE'})
