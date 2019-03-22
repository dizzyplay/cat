from rest_framework import serializers
from cat.models import Cat, Meal, CatStatus


class CatStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatStatus
        fields = ['title', 'value']


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['title', 'kcal']


class CatSerializer(serializers.ModelSerializer):
    meal = MealSerializer()
    status = CatStatusSerializer()

    class Meta:
        model = Cat
        fields = ['name', 'age', 'meal', 'status', 'created_at']


class CatStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatStatus
        fields = ['title', 'value']
