import grpc
import json
from google.protobuf.json_format import MessageToDict, MessageToJson


from stubs import shop_pb2 as ShopMessages
from stubs import shop_pb2_grpc as ShopServices



def getRetailerShops(retailer_id):
    channel = None
    try:
         with grpc.insecure_channel('localhost:8000') as channel:
            print("HERE")
            print(type(retailer_id))
            stub = ShopServices.ShopServiceStub(channel)
            print(stub)
            response = stub.GetShopList(ShopMessages.ShopRequest(retailer_id=retailer_id))
            dict_obj = MessageToDict(response, including_default_value_fields=True)
            print("fetch member by account response is , ", dict_obj)
            return dict_obj
    except Exception as ex:
        print("exception in GetShopList: " ,ex)
    finally:
        channel.close()
