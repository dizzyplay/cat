from graphene_django import DjangoObjectType
import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from .models import Cat, Meal, CatStatus


class CatStatusType(DjangoObjectType):
    class Meta:
        model = CatStatus


class MealType(DjangoObjectType):
    class Meta:
        model = Meal


class CatType(DjangoObjectType):
    class Meta:
        model = Cat


class CatNode(DjangoObjectType):
    class Meta:
        model = Cat
        filter_fields = {
            'name':['exact','icontains']
        }
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    # cat = graphene.Field(CatType, id=graphene.Int(), name=graphene.String())
    cata = relay.Node.Field(CatNode)
    all_cats = DjangoFilterConnectionField(CatNode)
    cats = graphene.List(CatType)
    meals = graphene.List(MealType)
    cat_status = graphene.List(CatStatusType)

    def resolve_cats(self, info):
        return Cat.objects.all()

    def resolve_meals(self, info):
        return Meal.objects.all()

    def resolve_cat_status(self, info):
        return CatStatus.objects.all()

    def resolve_cat(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Cat.objects.get(pk=id)
        if name is not None:
            return Cat.objects.get(name=name)
        return None
