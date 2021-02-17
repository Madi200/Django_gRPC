from django.urls import path


from .views import RetailerListAPIView

urlpatterns = [
    path('retailers/', RetailerListAPIView.as_view(), name='index'),
]
