from django.contrib.auth.models import Group, User
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from orderapp.serializers import (GroupSerializer, OrderSerializer,
                                  ProductSerializer, UserSerializer)

from .models import Order, Product


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """ override object behaviour to return ONLY the current user information """
        return self.request.user


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    """Restful Structure:
        | URL style      | HTTP Method | URL Nanme     | Action Function |
        |----------------|-------------|---------------|-----------------|
        | /person        | GET, POST   | person-list   | person-list     |
        | /person/<id>   | GET, DELETE | person-detail | person-detail   |
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # def perform_create(self, serializer):
    #     data = self.request.data
    #     product_id = data['product']
    #     new_product_detail = Product.objects.filter(id=product_id)
    #     new_product_detail.quantity_in_stock = 100
    #     new_product_detail.save()
    #     serializer.save(
    #         user_id=self.request.user,
    #         date_created=timezone.now()
    #     )


class UpdateOrders(APIView):

    def post(self, request):
        """
        Reduce stock quantity when an order is made.
        """
        product_id = request.data['product']
        # new_product_detail = get_object_or_404(Product, pk=product_id)
        new_product_detail = Product.objects.get(id=product_id)
        new_product_detail.quantity_in_stock -= 1
        new_product_detail.save()
        serializer = ProductSerializer(new_product_detail)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
