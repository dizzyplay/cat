from graphene import Schema, ObjectType
from .query import Queries
from .mutation import Mutations

schema = Schema(query=Queries, mutation=Mutations)
