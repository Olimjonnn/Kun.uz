from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from main.models import *
from main.serializer import *       

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]


class CategoryCityView(viewsets.ModelViewSet):
    queryset = CategoryCity.objects.all()
    serializer_class = CategoryCitySerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

class ViderCategoryView(viewsets.ModelViewSet):
    queryset = ViderCategory.objects.all()
    serializer_class = ViderCategorySerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]


class NewsView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    @action(["GET"], detail=False)
    def find(self, request):
        try:
            category = request.GET.get("category")
            new = News.objects.filter(category_id=category)
            ne = NewsSerializer(new, many=True)
            return Response(ne.data)
        except Exception as arr:
            data = {
                "error": f"{arr}"
            }    
            return Response(data)
    
    @action(["GET"], detail=False)
    def find_city(self, request):
        try:
            category_city = request.GET.get("category_city")
            new = News.objects.filter(category_city_id=category_city)
            ne = NewsSerializer(new, many=True)
            return Response(ne.data)
        except Exception as arr:
            data = {
                "error": f"{arr}"
            }    
            return Response(data)
    


