from .types import CatType
from . import resolver as resolve
import graphene
from graphene_django.filter import DjangoFilterConnectionField


class Query(graphene.ObjectType):
    cats = DjangoFilterConnectionField(CatType, resolver=resolve.cats)
    cat = graphene.relay.Node.Field(CatType)