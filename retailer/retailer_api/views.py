from django.http import HttpResponse

from .serializers  import RetailerSerializer
from rest_framework.views import APIView

from rest_framework.response import Response
from .clients import getRetailerShops

class RetailerListAPIView(APIView):

    def get(self, request):
        print(request.GET.get('retailer_id'))
        print(request)
        vvv = getRetailerShops(int(request.GET.get('retailer_id')))
        print(vvv)
        # queryset = Retailer.objects.all()
        # serializer = RetailerSerializer(queryset, many=True)
        return Response({'data':vvv, 'msg':'In Progress'}, status=200)
