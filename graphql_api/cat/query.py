from .types import CatType
from . import resolver as resolve
import graphene


class Query(graphene.ObjectType):
    cats = graphene.List(CatType, resolver=resolve.cats)
