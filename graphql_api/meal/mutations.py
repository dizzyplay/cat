import graphene
from cat.models import Meal
from .types import DjangoMealType


class CreateMeal(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        kcal = graphene.String()

    meal = graphene.Field(DjangoMealType)

    @staticmethod
    def mutate(root, info, **kwargs):
        print(kwargs['title'])
        meal = Meal.objects.create(title=kwargs['title'], kcal=kwargs['kcal'])
        return DjangoMealType(meal=meal)


class Mutation(graphene.ObjectType):
    create_meal = CreateMeal.Field()
