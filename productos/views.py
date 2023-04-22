from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Categoria, Ingrediente, Ingredientes_preparacion, Preparacion
from .serializers import CategoriaSerializer, IngredienteSerializer, Ingredientes_preparacionSerializer, PreparacionSerializer

# Create your views here.
#GET, POST PUT DELETE CATEGORIAS-------------------------------------------------------------------------

@api_view(['GET','POST','DELETE'])
def categoria_list(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        categoria_serializer = CategoriaSerializer(categorias,many=True)
        return Response(categoria_serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        categoria_data = JSONParser().parse(request)
        categoria_serializer = CategoriaSerializer(data=categoria_data)
        if categoria_serializer.is_valid():
            categoria_serializer.save()
            return Response(categoria_serializer.data,status=status.HTTP_201_CREATED)
        return Response(categoria_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Categoria.objects.all().delete()
        return Response({'message:','{} Categorias han sido eliminadas de la base de datos'.format(count[0])},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def categoria_detail(request,id_cat):
    try:
        categoria = Categoria.objects.get(id_cat=id_cat)
    except Categoria.DoesNotExist:
        return Response({'messaje':'La categoria buscada no existe en nuestros registros'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        categoria_serializer = CategoriaSerializer(categoria)
        return Response(categoria_serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        categoria_data = JSONParser().parse(request)
        categoria_serializer = CategoriaSerializer(categoria, data=categoria_data)
        if categoria_serializer.is_valid():
            categoria_serializer.save()
            return Response(categoria_serializer.data,status=status.HTTP_200_OK)
        return Response(categoria_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        categoria.delete()
        return Response({'message':'Categoria eliminada correctamente'}, status=status.HTTP_200_OK)
    
#GET, POST PUT DELETE INGREDIENTES-------------------------------------------------------------------------

@api_view(['GET','POST','DELETE'])
def ingrediente_list(request):
    if request.method == 'GET':
        ingredientes = Ingrediente.objects.all()
        ingrediente_serializer = IngredienteSerializer(ingredientes,many=True)
        return Response(ingrediente_serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        ingrediente_data = JSONParser().parse(request)
        ingrediente_serializer = IngredienteSerializer(data=ingrediente_data)
        if ingrediente_serializer.is_valid():
            ingrediente_serializer.save()
            return Response(ingrediente_serializer.data,status=status.HTTP_201_CREATED)
        return Response(ingrediente_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Ingrediente.objects.all().delete()
        return Response({'message:','{} Ingredientes han sido eliminados de la base de datos'.format(count[0])},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def ingrediente_detail(request,id_ingre):
    try:
        ingrediente = Ingrediente.objects.get(id_ingre=id_ingre)
    except Ingrediente.DoesNotExist:
        return Response({'messaje':'El ingrediente buscado no existe en nuestros registros'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        ingrediente_serializer = IngredienteSerializer(ingrediente)
        return Response(ingrediente_serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        ingrediente_data = JSONParser().parse(request)
        ingrediente_serializer = IngredienteSerializer(ingrediente, data=ingrediente_data)
        if ingrediente_serializer.is_valid():
            ingrediente_serializer.save()
            return Response(ingrediente_serializer.data,status=status.HTTP_200_OK)
        return Response(ingrediente_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ingrediente.delete()
        return Response({'message':'Ingrediente eliminado correctamente'}, status=status.HTTP_200_OK)
    
#GET, POST PUT DELETE INGREDIENTES_PREPARACION?-------------------------------------------------------------------------

@api_view(['GET','POST','DELETE'])
def ingrediente_prep_list(request):
    if request.method == 'GET':
        ingredientes_prep = Ingredientes_preparacion.objects.all()
        ingrediente_prep_serializer = Ingredientes_preparacionSerializer(ingredientes_prep,many=True)
        return Response(ingrediente_prep_serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        ingrediente_prep_data = JSONParser().parse(request)
        ingrediente_prep_serializer = IngredienteSerializer(data=ingrediente_prep_data)
        if ingrediente_prep_serializer.is_valid():
            ingrediente_prep_serializer.save()
            return Response(ingrediente_prep_serializer.data,status=status.HTTP_201_CREATED)
        return Response(ingrediente_prep_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Ingredientes_preparacion.objects.all().delete()
        return Response({'message:','{} Ingredientes_preparacion han sido eliminados de la base de datos'.format(count[0])},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def ingrediente_prep_detail(request,id_prep):
    try:
        ingrediente_prep = Ingredientes_preparacion.objects.get(id_prep=id_prep)
    except Ingrediente.DoesNotExist:
        return Response({'messaje':'El ingrediente de preparacion buscado no existe en nuestros registros'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        ingrediente_prep_serializer = Ingredientes_preparacionSerializer(ingrediente_prep)
        return Response(ingrediente_prep_serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        ingrediente_prep_data = JSONParser().parse(request)
        ingrediente_prep_serializer = Ingredientes_preparacionSerializer(ingrediente_prep, data=ingrediente_prep_data)
        if ingrediente_prep_serializer.is_valid():
            ingrediente_prep_serializer.save()
            return Response(ingrediente_prep_serializer.data,status=status.HTTP_200_OK)
        return Response(ingrediente_prep_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ingrediente_prep.delete()
        return Response({'message':'Ingrediente de preparacion eliminado correctamente'}, status=status.HTTP_200_OK)

#GET, POST PUT DELETE PREPARACIONES-------------------------------------------------------------------------

@api_view(['GET','POST','DELETE'])
def preparacion_list(request):
    if request.method == 'GET':
        preparaciones = Preparacion.objects.all()
        preparacion_serializer = PreparacionSerializer(preparaciones,many=True)
        return Response(preparacion_serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        preparacion_data = JSONParser().parse(request)
        preparacion_serializer = IngredienteSerializer(data=preparacion_data)
        if preparacion_serializer.is_valid():
            preparacion_serializer.save()
            return Response(preparacion_serializer.data,status=status.HTTP_201_CREATED)
        return Response(preparacion_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Preparacion.objects.all().delete()
        return Response({'message:','{} Preparaciones han sido eliminadas de la base de datos'.format(count[0])},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def preparacion_detail(request,id_prep):
    try:
        preparacion = Preparacion.objects.get(id_prep=id_prep)
    except Preparacion.DoesNotExist:
        return Response({'messaje':'La preparacion buscada no existe en nuestros registros'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        preparacion_serializer = IngredienteSerializer(preparacion)
        return Response(preparacion_serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        preparacion_data = JSONParser().parse(request)
        preparacion_serializer = IngredienteSerializer(preparacion, data=preparacion_data)
        if preparacion_serializer.is_valid():
            preparacion_serializer.save()
            return Response(preparacion_serializer.data,status=status.HTTP_200_OK)
        return Response(preparacion_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        preparacion.delete()
        return Response({'message':'Preparacion eliminada correctamente'}, status=status.HTTP_200_OK)