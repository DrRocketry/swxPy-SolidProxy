from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SWModelSerializer
from .models import SWModel

# Create your views here.

def front(request):
    context = { }
    return render(request, "index.html", context)


@api_view(['GET'])
def get_all_models(request):

    m = SWModel.objects.all()
    serializer = SWModelSerializer(m, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_models_hash(request):
    """Get the model hash to determine if open models have changed"""
    m = SWModel.objects.values_list('title', flat=True)
    h = hash(tuple(m))
    print(f'\thash: {h}')
    return Response(data={'h': h})