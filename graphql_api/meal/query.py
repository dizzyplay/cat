import graphene
from . import resolvers as resolve
from .types import MealType, StatusType


class Query(graphene.ObjectType):
    meal = graphene.List(MealType, resolver=resolve.all_meal)
    status = graphene.List(StatusType, resolver=resolve.all_status)
