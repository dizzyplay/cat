import graphene
from .resolvers import CreateMeal


class Mutation(graphene.ObjectType):
    create_meal = CreateMeal.Field()


