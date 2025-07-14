from django.http import HttpRequest
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from cinema.models import Movie
from cinema.serializers import MovieSerializer


@api_view(["GET", "POST"])
def movie_list(request: HttpRequest):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(instance=movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def movie_detail(request: HttpRequest, pk: int):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "GET":
        serializer = MovieSerializer(instance=movie)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = MovieSerializer(instance=movie, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == "DELETE":
        movie.delete()
        return Response(status.HTTP_204_NO_CONTENT)
