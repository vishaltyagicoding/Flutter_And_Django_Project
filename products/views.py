from rest_framework import generics
from .models import *
from .serializers import *
# Create your views here.

# Product Category Views
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class ProductsCategoryListView(generics.ListAPIView):
    queryset = Products_Category.objects.all()
    serializer_class = ProductsCategorySerializer

class ProductsCategoryDetailView(generics.RetrieveDestroyAPIView):
    queryset = Products_Category.objects.all()
    serializer_class = ProductsCategorySerializer


# Product Views
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Maker Views
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class MakerListView(generics.ListAPIView):
    queryset = Maker.objects.all()
    serializer_class = MakerSerializer

class MakerDetailView(generics.RetrieveDestroyAPIView):
    queryset = Maker.objects.all()
    serializer_class = MakerSerializer
