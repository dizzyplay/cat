from cat.models import Meal, CatStatus
from .types import DjangoMealType


def query_meals_resolver(root, info):
    return Meal.objects.all()


def query_statuses_resolver(root, info):
    return CatStatus.objects.all()


def query_get_meal(root, info, **kwargs):
    id = kwargs.get('id')
    title = kwargs.get('title')
    if id is not None:
        return Meal.objects.get(pk=id)
    if title is not None:
        return Meal.objects.get(title=title)
    return None



