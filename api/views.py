from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ExpenseSerializer

from .models import Expense


# Create your views here.


@api_view(['GET'])
def overview(request):
    api_urls = {
        'List': '/list/',
        'Detail View': '/expense-detail/<str:pk>/',
        'Create': '/expense-create/',
        'Update': '/expense-update/<str:pk>/',
        'Delete': '/expense-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def ExpenseList(request):
    items = Expense.objects.all().order_by('-id')
    serializer = ExpenseSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ExpenseDetail(request, pk):
    item = Expense.objects.get(id=pk)
    serial = ExpenseSerializer(item, many=False)
    return Response(serial.data)


@api_view(['PUT'])
def ExpenseCreate(request):
    serial = ExpenseSerializer(data=request.data)
    if serial.is_valid():
        serial.save()

    return Response(serial.data)


@api_view(['DELETE'])
def ExpenseDelete(request, pk):
    item = Expense.objects.get(id=pk)
    item.delete()

    return Response('Item successfully delete!')
