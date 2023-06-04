import json
from django.shortcuts import render, HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Compra, Item_compra
from .serializers import CompraSerializer, Item_compraSerializer
from productos.models import Ingrediente, Detalle_preparacion, Preparacion
from django.db.models import F
from django.core.paginator import Paginator, Page

# Create your views here.
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
def compra_detail(request,id_item_compra):
    try:
        compra = Compra.objects.get(id_item_compra=id_item_compra)
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
        item_compra_serializer = Item_compraSerializer(data=item_compra_data)
        if item_compra_serializer.is_valid():
            item_compra_serializer.save()
            return Response(item_compra_serializer.data,status=status.HTTP_201_CREATED)
        return Response(item_compra_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Item_compra.objects.all().delete()
        return Response({'message:','{} Items Compra han sido eliminadas de la base de datos'.format(count[0])},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def item_compra_detail(request,id_item_compra):
    try:
        item_compra = Item_compra.objects.get(id_item_compra=id_item_compra)
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

@api_view(['GET'])
def compras_recientes(request):
    compras = Compra.objects.all()
    datos = []
    for compra in compras:
        items = Item_compra.objects.filter(id_compra=compra.id_compra)
        compras_data = []
        for item in items:
            preparacion = Preparacion.objects.get(id_prep=item.id_prep)
            item_data = {
                'nombre_prep': preparacion.nombre_prep,
                'cantidad_item': item.cantidad_item
            }
            compras_data.append(item_data)

        compra_data = {
            'id_compra': compra.id_compra,
            'tipo_servicio_compra': compra.tipo_servicio_compra,
            'preparaciones': compras_data
        }
        datos.append(compra_data)
    return Response(datos, status=status.HTTP_200_OK)

@api_view(['GET'])
def compras_recientes_paginadas(request):
    compras = Compra.objects.all().order_by('-fecha_compra')  # Ordena por fecha_compra en orden descendente con el parametro -
    paginator = Paginator(compras, 3)# Divide los resultados en páginas de n cantidad de elementos

    page_number = request.GET.get('page') # Obtén el número de página de los parámetros de la solicitud
    page_obj = paginator.get_page(page_number) # Obtiene el objeto de página correspondiente al número de página

    datos = []
    for compra in page_obj: # Itera sobre los elementos de la página actual
        items = Item_compra.objects.filter(id_compra=compra.id_compra)
        compras_data = []
        for item in items:
            preparacion = Preparacion.objects.get(id_prep=item.id_prep)
            item_data = {
                'nombre_prep': preparacion.nombre_prep,
                'cantidad_item': item.cantidad_item
            }
            compras_data.append(item_data)

        compra_data = {
            'id_compra': compra.id_compra,
            'tipo_servicio_compra': compra.tipo_servicio_compra,
            'preparaciones': compras_data
        }
        datos.append(compra_data)

        '''
        response_data = {
        'count': paginator.count,
        'num_pages': paginator.num_pages,
        'current_page': page_number,
        'results': datos
        }
        '''
    return Response(datos, status=status.HTTP_200_OK)


@api_view(['POST'])
def item_compra_auto(request): 
    item_compra_data = JSONParser().parse(request)
    print('data_entrante: ', item_compra_data)
    for item in item_compra_data:
        id_prep = item['id_prep']
        cant_item = item['cantidad_item']
        try:
            det_prep = Detalle_preparacion.objects.filter(id_prep=id_prep)
            print('listado obj detalle prep: ', det_prep)
            for i in det_prep:
                totalEntrante = i.cantidad_necesaria * cant_item
                tipo_unidad_detalle_prep = i.tipo_unidad
                id_ingre_detalle_prep = i.id_ingre
                ingre = Ingrediente.objects.get(id_ingre=id_ingre_detalle_prep)
                stock_actual = ingre.stock_ingrediente
                tipo_unidad_ingrediente = ingre.tipo_unidad_ingrediente
                if tipo_unidad_detalle_prep == tipo_unidad_ingrediente:
                    if stock_actual - totalEntrante < 0:
                        return Response({'Resta no fue posible, revisar stock'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                    elif stock_actual - totalEntrante >= 0:
                        ingre.stock_ingrediente = stock_actual - totalEntrante
                        ingre.save()
                        return Response({'Stock actualizado correctamente correctamente'}, status=status.HTTP_200_OK)
                    else:
                        return Response({'Error interno'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Detalle_preparacion.DoesNotExist:
            return Response({'messaje':'El item compra buscado no existe en nuestros registros'},status=status.HTTP_404_NOT_FOUND)
    return Response(item_compra_data, status=status.HTTP_200_OK) 

