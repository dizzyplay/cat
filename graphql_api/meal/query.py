import graphene
from . import resolvers as resolve
from .types import DjangoMealType, DjangoCatStatusType
from graphene_django.filter import DjangoFilterConnectionField

class Query(graphene.ObjectType):
    all_meal =DjangoFilterConnectionField(DjangoMealType, resolver=resolve.query_meals_resolver)
    all_status = graphene.List(DjangoCatStatusType, resolver=resolve.query_statuses_resolver)
    meal = graphene.Field(DjangoMealType, id=graphene.String(), title=graphene.String(), resolver=resolve.query_get_meal)
