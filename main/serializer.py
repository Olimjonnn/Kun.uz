from rest_framework import serializers
from main.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = "__all__"

class CategoryCitySerializer(serializers.ModelSerializer):
    class Meta():
        model = CategoryCity
        fields = "__all__"

class NewsSerializer(serializers.ModelSerializer):
    class Meta():
        model = News
        fields = "__all__"

class ViderCategorySerializer(serializers.ModelSerializer):
    class Meta():
        model = ViderCategory
        fields = "__all__"

