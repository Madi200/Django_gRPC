from django.http import HttpResponse

from .serializers  import ShopSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  status

class ShopListAPIView(APIView):

    def get(self, request):
        queryset = Shop.objects.all()
        serializer = ShopSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request, *args, **kwargs):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
