from django.urls import path


from .views import ShopListAPIView

urlpatterns = [
    path('shops/', ShopListAPIView.as_view(), name='index'),
]
