from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from orderapp.serializers import UserSerializer, GroupSerializer, ProductSerializer
from .models import Product


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
    permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    """Restful Structure:
        | URL style      | HTTP Method | URL Nanme     | Action Function |
        |----------------|-------------|---------------|-----------------|
        | /person        | GET, POST   | person-list   | person-list     |
        | /person/<id>   | GET, DELETE | person-detail | person-detail   |
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
