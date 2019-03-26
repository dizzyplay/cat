from graphene_django import DjangoObjectType
from cat.models import Meal, CatStatus
import graphene


class DjangoMealType(DjangoObjectType):
    class Meta:
        model = Meal
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (graphene.relay.Node,)


class DjangoCatStatusType(DjangoObjectType):
    class Meta:
        model = CatStatus
