from django.http import HttpResponse
from django.shortcuts import render
from .serializers import AuthorSerializer
from author.models import Author
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.
def index(request):
    return HttpResponse('<h1>Главная</h1>')
def about(request):
    return HttpResponse('<h1>О авторах</h1>')

@api_view(['GET'])
def get_authors(request):
    queryset = Author.objects.all()
    serializer = AuthorSerializer(queryset,many = True)
    return Response(serializer.data)

@api_view(['POST'])
def create_product(request):
    serializer = AuthorSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','PATCH','DELETE'])
def f(request,pk):
    try:
        product = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AuthorSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AuthorSerializer(product,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)