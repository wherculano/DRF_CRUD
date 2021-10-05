from django.shortcuts import render
from .models import Aluno
from .serializers import AlunoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def AlunoList(request):
    alunos = Aluno.objects.all()
    serializer = AlunoSerializer(alunos, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def AlunoPost(request):
    serializer = AlunoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def AlunoPut(request, pk):
    alunos = Aluno.objects.get(id=pk)
    serializer = AlunoSerializer(alunos, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def AlunoDelete(request, pk):
    alunos = Aluno.objects.get(id=pk)
    alunos.delete()
    return Response(f"Aluno {alunos.data} apagado!")

