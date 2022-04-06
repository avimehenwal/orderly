from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from orderapp.serializers import UserSerializer, GroupSerializer, ProductSerializer, OrderSerializer
from .models import Product, Order
from rest_framework.views import APIView
from rest_framework.response import Response
import json


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


class ListOrders(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all orders.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)

    def post(self, request):
        """
        Make an orders.
        """
        # serializer = SnippetSerializer(data=request.data)
        serializer = json.loads(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
