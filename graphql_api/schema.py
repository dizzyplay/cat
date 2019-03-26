from graphene import Schema
from .query import Queries
from .mutation import Mutations

schema = Schema(query=Queries, mutation=Mutations)


