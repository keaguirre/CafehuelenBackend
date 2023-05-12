from django.shortcuts import render, HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Categoria, Ingrediente, Detalle_preparacion, Preparacion
from .serializers import CategoriaSerializer, Detalle_prep_relatedSerializer, IngredienteSerializer, Detalle_preparacionSerializer, PreparacionSerializer, PreparacionCatSerializer
from django.db.models import Count

# Create your views here.
#GET, POST PUT DELETE CATEGORIAS-------------------------------------------------------------------------

@api_view(['GET','POST','DELETE'])
def categoria_list(request):
    # if request.method == 'GET':
    #     categorias = Categoria.objects.all()
        
    #     categoria_serializer = CategoriaSerializer(categorias,many=True)
    #     return Response(categoria_serializer.data,status=status.HTTP_200_OK)

    if request.method == 'GET':
        categorias = Categoria.objects.all().filter(estado=True)
        categoria_serializer = CategoriaSerializer(categorias,many=True)
        return Response(categoria_serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        categoria_data = JSONParser().parse(request)
        categoria_serializer = CategoriaSerializer(data=categoria_data)
        if categoria_serializer.is_valid():
            categoria_serializer.save()
            content = 'Categoria '+ categoria_serializer.data['nombre_cat']+ ' Creada'
            return Response(content, status=status.HTTP_201_CREATED)
            # return Response({'Categoria creada correctamente'}, status=status.HTTP_201_CREATED)
        return Response(categoria_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Categoria.objects.all().delete()
        return Response({'message:','{} Categorias han sido eliminadas de la base de datos'.format(count[0])},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','PATCH','DELETE'])
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

    elif request.method == 'PATCH':
        categoria_data = JSONParser().parse(request)
        categoria_serializer = CategoriaSerializer(categoria, data=categoria_data, partial=True)
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
    # if request.method == 'GET':
    #     ingredientes = Ingrediente.objects.all()
    #     ingrediente_serializer = IngredienteSerializer(ingredientes,many=True)
    #     return Response(ingrediente_serializer.data,status=status.HTTP_200_OK)

    if request.method == 'GET':
        ingredientes = Ingrediente.objects.all().filter(estado=True)
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

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
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
    
    elif request.method == 'PATCH':
        ingrediente_data = JSONParser().parse(request)
        ingrediente_serializer = IngredienteSerializer(ingrediente, data=ingrediente_data, partial=True)
        if ingrediente_serializer.is_valid():
            ingrediente_serializer.save()
            return Response(ingrediente_serializer.data, status=status.HTTP_200_OK)
        return Response(ingrediente_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ingrediente.delete()
        return Response({'message':'Ingrediente eliminado correctamente'}, status=status.HTTP_200_OK)
    
#GET, POST PUT DELETE INGREDIENTES_PREPARACION?-------------------------------------------------------------------------

@api_view(['GET','POST','DELETE'])
def detalle_prep_list(request):
    # if request.method == 'GET':
    #     detalles_prep = Detalle_preparacion.objects.all()
    #     detalle_prep_serializer = Detalle_preparacionSerializer(detalles_prep,many=True)
    #     return Response(detalle_prep_serializer.data,status=status.HTTP_200_OK)
    if request.method == 'GET':
        detalles_prep = Detalle_preparacion.objects \
        .select_related('id_prep', 'id_ingre').filter(estado=True) \
        .values(
            'id_detalle_prep',
            'id_prep__nombre_prep',
            'id_ingre__nombre_ingre',
            'cantidad_necesaria',
            'tipo_unidad',
            'estado'
        )
        detalle_prep_serializer = Detalle_prep_relatedSerializer(detalles_prep,many=True)
        return Response(detalle_prep_serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        detalle_prep_data = JSONParser().parse(request)
        detalle_prep_serializer = Detalle_preparacionSerializer(data=detalle_prep_data)
        if detalle_prep_serializer.is_valid():
            detalle_prep_serializer.save()
            return Response(detalle_prep_serializer.data,status=status.HTTP_201_CREATED)
        return Response(detalle_prep_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Detalle_preparacion.objects.all().delete()
        return Response({'message:','{} Detalles_preparacion han sido eliminados de la base de datos'.format(count[0])},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def detalle_prep_detail(request,id_detalle_prep):
    try:
        detalle_prep = Detalle_preparacion.objects.get(id_detalle_prep=id_detalle_prep)
    except Detalle_preparacion.DoesNotExist:                                                                                                                                                                                                                                                                                    
        return Response({'messaje':'El detalle de la preparación buscado no existe en nuestros registros'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        detalle_prep_serializer = Detalle_preparacionSerializer(detalle_prep)
        return Response(detalle_prep_serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        detalle_prep_data = JSONParser().parse(request)
        detalle_prep_serializer = Detalle_preparacionSerializer(detalle_prep, data=detalle_prep_data)
        if detalle_prep_serializer.is_valid():
            detalle_prep_serializer.save()
            return Response(detalle_prep_serializer.data,status=status.HTTP_200_OK)
        return Response(detalle_prep_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        detalle_prep_data = JSONParser().parse(request)
        detalle_prep_serializer = Detalle_preparacionSerializer(detalle_prep, data=detalle_prep_data, partial=True)
        if detalle_prep_serializer.is_valid():
            detalle_prep_serializer.save()
            return Response(detalle_prep_serializer.data, status=status.HTTP_200_OK)
        return Response(detalle_prep_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        detalle_prep.delete()
        return Response({'message':'Detalle de la preparación eliminado correctamente'}, status=status.HTTP_200_OK)

#GET, POST PUT DELETE PREPARACIONES-------------------------------------------------------------------------

@api_view(['GET','POST','DELETE'])
def preparacion_list(request):
    # if request.method == 'GET': #LISTA
    #     preparaciones = Preparacion.objects.all()
    #     preparacion_serializer = PreparacionSerializer(preparaciones,many=True)
    #     return Response(preparacion_serializer.data,status=status.HTTP_200_OK)
    
    if request.method == 'GET':
        # preparaciones = Preparacion.objects.all()
        preparaciones = Preparacion.objects \
        .select_related('id_cat_prep').filter(estado=True) \
        .values(
            'id_prep', 
            'nombre_prep',
            'descripcion_prep',
            'imagen_prep',
            'id_cat_prep__nombre_cat',
            'precio_prep',
            'estado'
        )
        preparacion_serializer = PreparacionCatSerializer(preparaciones,many=True)
        return Response(preparacion_serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST': #CREA
        preparacion_data = JSONParser().parse(request)
        preparacion_serializer = PreparacionSerializer(data=preparacion_data)
        if preparacion_serializer.is_valid():
            preparacion_serializer.save()
            return Response(preparacion_serializer.data,status=status.HTTP_201_CREATED)
        return Response(preparacion_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE': #ELIMINA
        count = Preparacion.objects.all().delete()
        return Response({'message:','{} Preparaciones han sido eliminadas de la base de datos'.format(count[0])},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def preparacion_detail(request,id_prep):
    try:
        preparacion = Preparacion.objects.get(id_prep=id_prep)
    except Preparacion.DoesNotExist:
        return Response({'messaje':'La preparacion buscada no existe en nuestros registros'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        preparacion_serializer = PreparacionSerializer(preparacion)
        return Response(preparacion_serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        preparacion_data = JSONParser().parse(request)
        preparacion_serializer = PreparacionSerializer(preparacion, data=preparacion_data)
        if preparacion_serializer.is_valid():
            preparacion_serializer.save()
            return Response(preparacion_serializer.data,status=status.HTTP_200_OK)
        return Response(preparacion_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        preparacion_data = JSONParser().parse(request)
        preparacion_serializer = PreparacionSerializer(preparacion, data=preparacion_data, partial=True)
        if preparacion_serializer.is_valid():
            preparacion_serializer.save()
            return Response(preparacion_serializer.data,status=status.HTTP_200_OK)
        return Response(preparacion_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        preparacion.delete()
        return Response({'message':'Preparacion eliminada correctamente'}, status=status.HTTP_200_OK)
             
#---------------------------------------------------------------------------------------
@api_view(['GET'])
def cat_find_id(request, nombre_cat): #ESTO RETORNA EL NOMBRE CAT ENCONTRADO
    try:
        categoria = Categoria.objects.get(nombre_cat=nombre_cat)
    except Categoria.DoesNotExist:
        return Response({'messaje':'La categoria buscada no existe en nuestros registros'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET': #ESTE FILTRA LOS TRUE
        categoria_find_serializer = CategoriaSerializer(categoria)
        if (categoria_find_serializer['estado'].value == True):
            return Response(categoria_find_serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({'messaje':'La categoria buscada no existe en nuestros registros'},status=status.HTTP_404_NOT_FOUND)

#Vista deshabilitados
@api_view(['GET'])
def get_disabled_catList(request):
    if request.method == 'GET':
        categorias = Categoria.objects.filter(estado=False)
        datos = []
        for categoria in categorias:
            preparaciones = Preparacion.objects.filter(id_cat_prep=categoria.id_cat) #listado de preparaciones por categoria
            preparaciones_data = [{'nombre_prep': prep.nombre_prep} for prep in preparaciones]
            categoria_data = {
                'id_cat': categoria.id_cat,
                'nombre_cat': categoria.nombre_cat,
                'estado': categoria.estado,
                'cantidad_preparaciones': len(preparaciones_data),
                'preparaciones': preparaciones_data,
            }
            datos.append(categoria_data)
        return Response(datos)