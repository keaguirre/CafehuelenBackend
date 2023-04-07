from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Cupon, Compra, Item_compra
from .serializers import CuponSerializer, CompraSerializer, Item_compraSerializer

# Create your views here.
#GET, POST PUT DELETE CUPONES-------------------------------------------------------------------------

@api_view(['GET','POST','DELETE'])
def cupon_list(request):
    if request.method == 'GET':
        cupones = Cupon.objects.all()
        cupon_serializer = CuponSerializer(cupones,many=True)
        return Response(cupon_serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        cupon_data = JSONParser().parse(request)
        cupon_serializer = CuponSerializer(data=cupon_data)
        if cupon_serializer.is_valid():
            cupon_serializer.save()
            return Response(cupon_serializer.data,status=status.HTTP_201_CREATED)
        return Response(cupon_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Cupon.objects.all().delete()
        return Response({'message:','{} Cupones han sido eliminados de la base de datos'.format(count[0])},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def cupon_detail(request,nombre_cup):
    try:
        cupon = Cupon.objects.get(nombre_cup=nombre_cup)
    except Cupon.DoesNotExist:
        return Response({'messaje':'El cupon buscado no existe en nuestros registros'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        cupon_serializer = CuponSerializer(cupon)
        return Response(cupon_serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        cupon_data = JSONParser().parse(request)
        cupon_serializer = CuponSerializer(data=cupon_data)
        if cupon_serializer.is_valid():
            cupon_serializer.save()
            return Response(cupon_serializer.data,status=status.HTTP_200_OK)
        return Response(cupon_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cupon.delete()
        return Response({'message':'cupon eliminado correctamente'}, status=status.HTTP_200_OK)

#GET, POST PUT DELETE COMPRA-------------------------------------------------------------------------

@api_view(['GET','POST','DELETE'])
def compra_list(request):
    if request.method == 'GET':
        compras = Compra.objects.all()
        compra_serializer = CompraSerializer(compras,many=True)
        return Response(compra_serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        compra_data = JSONParser().parse(request)
        compra_serializer = CompraSerializer(data=compra_data)
        if compra_serializer.is_valid():
            compra_serializer.save()
            return Response(compra_serializer.data,status=status.HTTP_201_CREATED)
        return Response(compra_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Compra.objects.all().delete()
        return Response({'message:','{} Compras han sido eliminadas de la base de datos'.format(count[0])},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def compra_detail(request,id_compra):
    try:
        compra = Compra.objects.get(id_compra=id_compra)
    except Compra.DoesNotExist:
        return Response({'messaje':'La compra buscada no existe en nuestros registros'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        compra_serializer = CompraSerializer(compra)
        return Response(compra_serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        compra_data = JSONParser().parse(request)
        compra_serializer = CompraSerializer(data=compra_data)
        if compra_serializer.is_valid():
            compra_serializer.save()
            return Response(compra_serializer.data,status=status.HTTP_200_OK)
        return Response(compra_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        compra.delete()
        return Response({'message':'Compra eliminada correctamente'}, status=status.HTTP_200_OK)

#GET, POST PUT DELETE ITEM_COMPRA-------------------------------------------------------------------------

@api_view(['GET','POST','DELETE'])
def item_compra_list(request):
    if request.method == 'GET':
        item_compras = Item_compra.objects.all()
        item_compra_serializer = Item_compraSerializer(item_compras,many=True)
        return Response(item_compra_serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        item_compra_data = JSONParser().parse(request)
        item_compra_serializer = CompraSerializer(data=item_compra_data)
        if item_compra_serializer.is_valid():
            item_compra_serializer.save()
            return Response(item_compra_serializer.data,status=status.HTTP_201_CREATED)
        return Response(item_compra_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Item_compra.objects.all().delete()
        return Response({'message:','{} Items Compra han sido eliminadas de la base de datos'.format(count[0])},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def item_compra_detail(request,id_prep):
    try:
        item_compra = Item_compra.objects.get(id_prep=id_prep)
    except Item_compra.DoesNotExist:
        return Response({'messaje':'El item compra buscado no existe en nuestros registros'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        item_compra_serializer = Item_compraSerializer(item_compra)
        return Response(item_compra_serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        item_compra_data = JSONParser().parse(request)
        item_compra_serializer = Item_compraSerializer(data=item_compra_data)
        if item_compra_serializer.is_valid():
            item_compra_serializer.save()
            return Response(item_compra_serializer.data,status=status.HTTP_200_OK)
        return Response(item_compra_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item_compra.delete()
        return Response({'message':'Item compra eliminado correctamente'}, status=status.HTTP_200_OK)
