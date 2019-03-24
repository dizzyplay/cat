from cat.models import Meal, CatStatus, Cat
import graphene
from .types import MealType


def all_meal(root, info):
    return Meal.objects.all()


def all_status(root, info):
    return CatStatus.objects.all()


class CreateMeal(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        kcal = graphene.String()

    meal = graphene.Field(MealType)

    def mutate(self, info, title, kcal):
        meal = Meal.objects.create(title=title, kcal=kcal)
        return CreateMeal(meal=meal)
