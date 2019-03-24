from graphene_django import DjangoObjectType
from cat.models import Cat


class CatType(DjangoObjectType):
    class Meta:
        model = Cat
