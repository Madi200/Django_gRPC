import grpc
import json
from google.protobuf.json_format import MessageToDict, MessageToJson

from stubs import shop_pb2 as ShopMessages
from stubs import shop_pb2_grpc as ShopServices

from ..models import Shop
from ..serializers import ShopSerializer


class ShopReadService:

    @staticmethod
    def get_retailer_shops(retailer_id:None):
        response = {
            "Success": False,
            "ExceptionString": "",
            "data": []}
        try:
            queryset = Shop.objects.filter(retailer_id=retailer_id)
            serializer = ShopSerializer(queryset, many=True)
            response['Success'] = True
            response['ExceptionString'] = ""
            response['data'] = serializer.data
            return response
        except Exception as e:
            response['Success'] = False
            response['ExceptionString'] = str(e)
            response['data'] = []
