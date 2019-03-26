import graphene
import importlib
from inspect import getmembers, isclass
import os


class MutationsAbstract(graphene.ObjectType):
    pass


mutations_base_classes = [MutationsAbstract]
current_directory = os.path.dirname(os.path.abspath(__file__))
current_module = current_directory.split('/')[-1]
subdirectories = [
    x
    for x in os.listdir(current_directory)
    if os.path.isdir(os.path.join(current_directory, x)) and
       x != '__pycache__'
]
for directory in subdirectories:
    print(f'{current_module}.{directory}.mutations')
    try:
        module = importlib.import_module(f'{current_module}.{directory}.mutations')
        if module:
            classes = [x for x in getmembers(module, isclass)]
            mutations = [x[1] for x in classes if 'Mutation' in x[0]]
            mutations_base_classes += mutations
    except ModuleNotFoundError:
        pass

mutations_base_classes = mutations_base_classes[::-1]
properties = {}
for base_class in mutations_base_classes:
    properties.update(base_class.__dict__['_meta'].fields)

Mutations = type(
    'Mutations',
    tuple(mutations_base_classes),
    properties
)
