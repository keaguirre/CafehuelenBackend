from datetime import date, datetime, timedelta
import datetime
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
from django.db.models.functions import Extract
from django.db.models import Count
from django.utils import timezone
from django.db import connection
from django.db.models.functions import ExtractWeek, ExtractMonth, ExtractYear
from django.db.models import Sum

DIAS_SEMANA = {
    'Monday': 'Lunes',
    'Tuesday': 'Martes',
    'Wednesday': 'Miércoles',
    'Thursday': 'Jueves',
    'Friday': 'Viernes',
    'Saturday': 'Sábado',
    'Sunday': 'Domingo',
}

MONTH_TRANSLATIONS = {
    1: 'Enero',
    2: 'Febrero',
    3: 'Marzo',
    4: 'Abril',
    5: 'Mayo',
    6: 'Junio',
    7: 'Julio',
    8: 'Agosto',
    9: 'Septiembre',
    10: 'Octubre',
    11: 'Noviembre',
    12: 'Diciembre',
}

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

#--------------------------------------Analiticas---------------------------------------------------------------------
@api_view(['GET'])
def cantidad_compras_hoy(request):
    today = date.today()
    tomorrow = today + timedelta(days=1)

    count = Compra.objects.filter(fecha_compra__gte=today, fecha_compra__lt=tomorrow).count()

    response_data = {
        'count': count
    }

    return Response(response_data, status=status.HTTP_200_OK)

    return Response({'fecha_hoy': fecha_actual_str, 'total_compra': total}, status=status.HTTP_200_OK)
@api_view(['GET']) #Retorna el nombre del dia y la cantidad de compras por dia
def compras_dia_semana(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT rtrim(TO_CHAR(fecha_compra, 'Day')) AS dia_semana, COUNT(id_compra) AS total_compras
            FROM compras_compra
            WHERE fecha_compra >= date_trunc('week', CURRENT_DATE)
                AND fecha_compra < date_trunc('week', CURRENT_DATE) + INTERVAL '1 week'
            GROUP BY dia_semana
            ORDER BY dia_semana
        """)
        rows = cursor.fetchall()

    # Preparar los datos de respuesta con traducción de días de la semana
    data = []
    for row in rows:
        dia_semana, total_compras = row
        dia_semana_es = DIAS_SEMANA.get(dia_semana, dia_semana)  # Obtener traducción del diccionario
        data.append({
            'dia_semana': dia_semana_es,
            'total_compras': total_compras,
        })
    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def total_compras_mes(request):
    total_compras = Compra.objects.filter(
        fecha_compra__month=timezone.now().month,
        fecha_compra__year=timezone.now().year
    ).aggregate(total_compras=Count('id_compra'))

    return Response({'total_compras_mes_actual': total_compras['total_compras']}, status=status.HTTP_200_OK)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection

@api_view(['GET'])
def total_compras_mes_x_semana(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                CAST(date_part('W', fecha_compra) - date_part('W', date_trunc('month', CURRENT_DATE)) + 1 AS INTEGER) AS semana_del_mes,
                CAST(EXTRACT(MONTH FROM fecha_compra) AS INTEGER) AS mes,
                COUNT(cc.id_compra) AS total_compras
            FROM compras_compra cc
            WHERE EXTRACT(MONTH FROM fecha_compra) = EXTRACT(MONTH FROM CURRENT_DATE)
                AND EXTRACT(YEAR FROM fecha_compra) = EXTRACT(YEAR FROM CURRENT_DATE)
            GROUP BY mes, semana_del_mes
            ORDER BY mes, semana_del_mes
        """)
        results = cursor.fetchall()

    data = []
    for row in results:
        semana_del_mes, mes, total_compras = row
        mes_traducido = MONTH_TRANSLATIONS.get(mes, mes)
        data.append({
            'semana_del_mes': semana_del_mes,
            'mes': mes,
            'nombre_mes': mes_traducido,
            'total_compras': total_compras,
        })

    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def total_compras_mes_anterior_x_semana(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                CAST(date_part('W', fecha_compra) - date_part('W', date_trunc('month', CURRENT_DATE)) + 1 AS INTEGER) AS semana_del_mes,
                CAST(EXTRACT(MONTH FROM fecha_compra) AS INTEGER) AS mes,
                COUNT(cc.id_compra) AS total_compras
            FROM compras_compra cc
            WHERE EXTRACT(MONTH FROM fecha_compra) = EXTRACT(MONTH FROM CURRENT_DATE - INTERVAL '1 month' )
                AND EXTRACT(YEAR FROM fecha_compra) = EXTRACT(YEAR FROM CURRENT_DATE)
            GROUP BY mes, semana_del_mes
            ORDER BY mes, semana_del_mes
        """)
        results = cursor.fetchall()

    data = []
    for row in results:
        semana_del_mes, mes, total_compras = row
        mes_traducido = MONTH_TRANSLATIONS.get(mes, mes)
        data.append({
            'semana_del_mes': semana_del_mes,
            'mes': mes,
            'nombre_mes': mes_traducido,
            'total_compras': total_compras,
        })

    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def total_compras_semana_anual(request):
    with connection.cursor() as cursor:
        query = """
            SELECT CAST(EXTRACT(WEEK FROM fecha_compra) AS INTEGER) AS semana, COUNT(cc.id_compra) AS total_compras
            FROM compras_compra cc
            WHERE EXTRACT(MONTH FROM fecha_compra) = EXTRACT(MONTH FROM CURRENT_DATE)
                AND EXTRACT(YEAR FROM fecha_compra) = EXTRACT(YEAR FROM CURRENT_DATE)
            GROUP BY semana
            ORDER BY semana
        """
        cursor.execute(query)
        rows = cursor.fetchall()

    data = [{'semana': row[0], 'total_compras': row[1]} for row in rows]

    return Response(data)

@api_view(['GET'])
def compras_por_mes_anual(request):
    with connection.cursor() as cursor:
        query = """
            SELECT EXTRACT(MONTH FROM fecha_compra)::INTEGER AS mes, COUNT(cc.id_compra) AS total_compras
            FROM compras_compra cc
            WHERE EXTRACT(MONTH FROM fecha_compra) = EXTRACT(MONTH FROM CURRENT_DATE)
                AND EXTRACT(YEAR FROM fecha_compra) = EXTRACT(YEAR FROM CURRENT_DATE)
            GROUP BY mes
            ORDER BY mes
        """
        cursor.execute(query)
        rows = cursor.fetchall()

    data = [{'mes': MONTH_TRANSLATIONS[row[0]], 'total_compras': row[1]} for row in rows]

    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def total_compras_hoy(request):
    fecha_actual = timezone.now().date()
    fecha_siguiente = fecha_actual + timedelta(days=1)
    
    total_compra_hoy = Compra.objects.filter(fecha_compra__gte=fecha_actual, fecha_compra__lt=fecha_siguiente).aggregate(total_compra_hoy=Sum('total_compra'))
    total = total_compra_hoy['total_compra_hoy'] or 0

    fecha_actual_str = fecha_actual.strftime("%d/%m/%Y")

    return Response({'fecha_hoy': fecha_actual_str, 'total_compra': total}, status=status.HTTP_200_OK)

@api_view(['GET'])
def sum_total_compra_week(request):
    fecha_actual = timezone.now().date()
    fecha_inicio_semana = fecha_actual - timedelta(days=fecha_actual.weekday())
    fecha_fin_semana = fecha_inicio_semana + timedelta(days=7)

    total_compra_week = Compra.objects.filter(fecha_compra__gte=fecha_inicio_semana, fecha_compra__lt=fecha_fin_semana).aggregate(total_compra_week=Sum('total_compra'))
    total = total_compra_week['total_compra_week'] or 0

    return Response({'total_compra_semanal': total}, status=status.HTTP_200_OK)

@api_view(['GET'])
def total_compra_diaria_semanal(request):    
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT rtrim(TO_CHAR(fecha_compra, 'Day')) AS dia_semana, sum(total_compra) AS total_compras
            FROM compras_compra
            WHERE fecha_compra >= date_trunc('week', CURRENT_DATE)
                AND fecha_compra < date_trunc('week', CURRENT_DATE) + INTERVAL '1 week'
            GROUP BY dia_semana
            ORDER BY dia_semana
        """)
        results = cursor.fetchall()

    response_data = []
    for row in results:
        dia_semana = row[0]
        total_compras = row[1]
        dia_semana_traducido = DIAS_SEMANA.get(dia_semana, dia_semana)
        response_data.append({
            'dia_semana': dia_semana_traducido,
            'total_compras': total_compras
        })
    return Response(response_data, status=status.HTTP_200_OK)

@api_view(['GET'])
def total_compra_semanal_anual(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT EXTRACT(WEEK FROM fecha_compra) AS semana, sum(cc.total_compra) AS total_compras
            FROM compras_compra cc
            WHERE EXTRACT(MONTH FROM fecha_compra) = EXTRACT(MONTH FROM CURRENT_DATE)
                AND EXTRACT(YEAR FROM fecha_compra) = EXTRACT(YEAR FROM CURRENT_DATE)
            GROUP BY semana
            ORDER BY semana
        """)
        results = cursor.fetchall()

    response_data = []
    for row in results:
        semana = row[0]
        total_compras = row[1]
        response_data.append({
            'semana': int(semana),
            'total_compras': total_compras
        })

    return Response(response_data, status=status.HTTP_200_OK)

@api_view(['GET'])
def total_compra_semanal_mes(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                date_part('W', fecha_compra) - date_part('W', date_trunc('month', CURRENT_DATE)) + 1 AS semana_del_mes,
                EXTRACT(MONTH FROM fecha_compra) AS mes,
                sum(cc.total_compra) AS total_compras
            FROM compras_compra cc
            WHERE EXTRACT(MONTH FROM fecha_compra) = EXTRACT(MONTH FROM CURRENT_DATE)
                AND EXTRACT(YEAR FROM fecha_compra) = EXTRACT(YEAR FROM CURRENT_DATE)
            GROUP BY mes, semana_del_mes
            ORDER BY mes, semana_del_mes
        """)
        results = cursor.fetchall()

    response_data = []
    for row in results:
        semana_del_mes = int(row[0])
        mes = int(row[1])
        total_compras = row[2]
        mes_nombre = MONTH_TRANSLATIONS.get(mes, '')
        response_data.append({
            'semana_del_mes': semana_del_mes,
            'mes': mes_nombre,
            'total_compras': total_compras
        })

    return Response(response_data, status=status.HTTP_200_OK)

@api_view(['GET'])
def total_compra_semanal_mes_anterior(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                date_part('W', fecha_compra) - date_part('W', date_trunc('month', CURRENT_DATE)) + 1 AS semana_del_mes,
                EXTRACT(MONTH FROM fecha_compra) AS mes,
                sum(cc.total_compra) AS total_compras
            FROM compras_compra cc
            WHERE EXTRACT(MONTH FROM fecha_compra) = EXTRACT(MONTH FROM CURRENT_DATE - INTERVAL '1 month' )
                AND EXTRACT(YEAR FROM fecha_compra) = EXTRACT(YEAR FROM CURRENT_DATE)
            GROUP BY mes, semana_del_mes
            ORDER BY mes, semana_del_mes
        """)
        results = cursor.fetchall()

    response_data = []
    for row in results:
        semana_del_mes = int(row[0])
        mes = int(row[1])
        total_compras = row[2]
        mes_nombre = MONTH_TRANSLATIONS.get(mes, '')
        response_data.append({
            'semana_del_mes': semana_del_mes,
            'mes': mes_nombre,
            'total_compras': total_compras
        })

    return Response(response_data, status=status.HTTP_200_OK)

@api_view(['GET'])
def total_compras_por_mes_anual(request):
    with connection.cursor() as cursor:
        query = """
            SELECT EXTRACT(MONTH FROM fecha_compra)::INTEGER AS mes, sum(cc.total_compra) AS total_compras
            FROM compras_compra cc
            WHERE EXTRACT(MONTH FROM fecha_compra) = EXTRACT(MONTH FROM CURRENT_DATE)
                AND EXTRACT(YEAR FROM fecha_compra) = EXTRACT(YEAR FROM CURRENT_DATE)
            GROUP BY mes
            ORDER BY mes
        """
        cursor.execute(query)
        rows = cursor.fetchall()

    data = [{'mes': MONTH_TRANSLATIONS[row[0]], 'total_compras': row[1]} for row in rows]

    return Response(data, status=status.HTTP_200_OK)