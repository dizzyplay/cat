from graphene_django import DjangoObjectType
from cat.models import Cat
import graphene


class CatType(DjangoObjectType):
    class Meta:
        model = Cat
        filter_fields = ['meal','status']
        interfaces = (graphene.relay.Node,)
