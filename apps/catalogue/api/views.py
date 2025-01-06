from rest_framework.decorators import api_view 
from rest_framework import status
from apps.catalogue.api.serializers import ProductSerializer 
from apps.catalogue.models import Product 
from rest_framework.response import Response
from django.http.response import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet



#function-based view
@api_view(['GET', 'POST'])
def product_list(request):
    #print(f'method {request.method}')
    if request.method == 'GET':
        products=get_list_or_404(Product)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

  
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#class-based view

class ProductListView(APIView):
    
    def get(self, request, format=None):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class ProductDetailView(APIView):
    def get(self, request, pk, format=None):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#generic class-based view 

class ProductListCreateView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = ProductSerializer 
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
class ProductDetailUpdateDestroyView(mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    serializer_class = ProductSerializer 
    queryset = Product.objects.all()

    def put(self, request, pk, *args, **kwargs):
        return super().update(request, pk, *args, **kwargs)    
    
    def get(self, request, pk, *args, **kwargs):
        return super().retrieve(request, pk, *args, **kwargs)
    
    def delete(self, request, pk, *args, **kwargs):
        return super().destroy(request, pk, *args, **kwargs)


#class-based view 

class ProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetailUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer 
    queryset = Product.objects.all()


