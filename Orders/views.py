
# Create your views here.

from rest_framework.viewsets import ModelViewSet
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.prefetch_related('items')
    serializer_class = OrderSerializer

