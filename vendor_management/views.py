from django.shortcuts import render
from rest_framework import generics
from .models import Vendor
from .serializers import VendorSerializer

class VendorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    
    def get_object(self):
        queryset = self.get_queryset()
        vendor_id = self.kwargs.get("vendor_id")
        obj = generics.get_object_or_404(queryset, id=vendor_id)
        return obj

