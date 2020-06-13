from .models import StudentI
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from rest_framework import status


# Create your views here.
def home(request):
    student_data = StudentI.objects.all()
    for i in student_data:
        print('name of student is:', i.name)
    return HttpResponse("this url is working")


@api_view(['GET','POST'])
def student_list(request):
    if request.method == 'GET':
        obj = StudentI.objects.all()
        serializer = StudentSerializer(obj, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=StudentSerializer(dat=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def detail(request,pk):
    try:
        obj = StudentI.objects.get(id=pk)
    except StudentI.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serializer = StudentSerializer(obj)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'PUT':
        serializer = StudentSerializer(dat=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

