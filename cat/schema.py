from graphene_django import DjangoObjectType
import graphene
from graphene import relay, Mutation
from graphene_django.filter import DjangoFilterConnectionField
from .models import Cat, Meal, CatStatus
from graphql_jwt.decorators import login_required
from django.contrib.auth import get_user_model



class MealType(DjangoObjectType):
    class Meta:
        model = Meal


class CreateMeal(Mutation):
    class Arguments:
        title = graphene.String()
        kcal= graphene.String()

    meal = graphene.Field(MealType)

    @staticmethod
    def mutate(root, info, title,kcal):
        print(info)
        meal = Meal.objects.create(title=title, kcal=kcal)
        return CreateMeal(meal=meal)


class CatStatusType(DjangoObjectType):
    class Meta:
        model = CatStatus


class CatType(DjangoObjectType):
    class Meta:
        model = Cat


class CatNode(DjangoObjectType):
    class Meta:
        model = Cat
        filter_fields = {
            'name': ['exact', 'icontains']
        }
        interfaces = (relay.Node,)


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class Query(graphene.ObjectType):
    cat = graphene.Field(CatType, id=graphene.Int(), name=graphene.String())
    all_cats = DjangoFilterConnectionField(CatNode)
    cats = graphene.List(CatType, token=graphene.String(required=True))
    meals = graphene.List(MealType)
    cat_status = graphene.List(CatStatusType)
    viewer = graphene.Field(UserType, token=graphene.String(required=True))

    @login_required
    def resolve_viewer(self, info, **kwargs):
        return info.context.user

    @login_required
    def resolve_cats(self, info, **kwargs):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception('no')
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
