from django.shortcuts import render
from  rest_framework.response import Response
from rest_framework.decorators import api_view

from . models import Movie
from . serial import MovieSerializer

@api_view(['GET'])
def movieList(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def movieDetail(request, pk):
    singlemovie = Movie.objects.get(id=pk)
    serializer = MovieSerializer(singlemovie, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def movieAdd(request):
    serialzer = MovieSerializer(data=request.data)

    if serialzer.is_valid():
        serialzer.save()
    return Response(serialzer.data)

@api_view(['POST'])
def movieUpdate(request, pk):
    singlemovie = Movie.objects.get(id=pk)
    serializer = MovieSerializer(instance=singlemovie, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def movieDelete(request, pk):
    singlemovie = Movie.objects.get(id=pk)
    singlemovie.delete()

    return Response('Deleted')
