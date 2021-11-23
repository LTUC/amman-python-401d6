from rest_framework import generics

from .models import Thing
from .serializers import ThingSerializer
from .permissions import IsOwnerOrReadOnly

class ThingList(generics.ListCreateAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer

class ThingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
    permission_classes = (IsOwnerOrReadOnly,)
