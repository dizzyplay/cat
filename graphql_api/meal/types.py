from graphene_django import DjangoObjectType
from cat.models import Meal, CatStatus


class MealType(DjangoObjectType):
    class Meta:
        model = Meal


class StatusType(DjangoObjectType):
    class Meta:
        model = CatStatus
