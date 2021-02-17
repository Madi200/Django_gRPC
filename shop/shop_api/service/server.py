
import grpc
import json
from google.protobuf.json_format import MessageToDict, MessageToJson

from stubs import shop_pb2 as ShopMessages
from stubs import shop_pb2_grpc as ShopServices

#from .services.read_service import get_retailer_shops
from ..models import Shop
from ..serializers import ShopSerializer

def get_retailer_shops(request):
    response = {
        "Success": False,
        "ExceptionString": "",
        "data": []}
    try:
        print('RRRRR', request)
        queryset = Shop.objects.filter(retailer_id=request['retailer_id'])
        print("Q", queryset)
        serializer = ShopSerializer(queryset, many=True)
        response['Success'] = True
        response['ExceptionString'] = ""
        response['data'] = serializer.data
        return response
    except Exception as e:
        response['Success'] = False
        response['ExceptionString'] = str(e)
        response['data'] = []

class Listener(ShopServices.ShopServiceServicer):
    print('SSSSSS')
    def GetShopList(self, request, context):
        print('Server mae a gaya')
        try:
            request = MessageToDict(
                request, preserving_proto_field_name=True, including_default_value_fields=True)
            response = get_retailer_shops(request)
            if response['Success']:
                return ShopMessages.ShopListResponse(data=response['data'])
            return []
        except Exception as e:
            print(e)



def grpc_hook(server):
    ShopServices.add_ShopServiceServicer_to_server(Listener(), server)
