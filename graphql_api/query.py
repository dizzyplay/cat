import graphene
import importlib
from inspect import getmembers, isclass
import os


class QueriesAbstract(graphene.ObjectType):
    pass


# 상속받을 클래스들
queries_base_classes = [QueriesAbstract]
# 현재 디렉토리의 절대경로
current_directory = os.path.dirname(os.path.abspath(__file__))
# 현재 디렉토리이름을 구해온다
current_module = current_directory.split('/')[-1]
# __pycache__를 제외한 현재 디렉토리의 하위 디렉토리를 리스트로 가져온다
subdirectories = [
    x
    for x in os.listdir(current_directory)
    if os.path.isdir(os.path.join(current_directory, x)) and
       x != '__pycache__'
]
# 하위디렉토리의 이름으로 모듈을 불러온다
for directory in subdirectories:
    # print(f'{current_module}.{directory}.query')
    try:
        module = importlib.import_module(f'{current_module}.{directory}.query')
        if module:
            # 묘듈의 클래스를 리스트로 가져온다. getmembers 는 튜플을 반환한다.
            classes = [x for x in getmembers(module, isclass)]
            # 클래스 이름에 Query가 있다면 리스트로 가져온다.
            queries = [x[1] for x in classes if 'Query' in x[0]]
            queries_base_classes += queries
    except ModuleNotFoundError:
        print('no module')
        pass

queries_base_classes = queries_base_classes[::-1]
# properties = {}
# for base_class in queries_base_classes:
#     print(base_class.__dict__['_meta'].fields)
#     properties.update(base_class.__dict__['_meta'].fields)
#     print(properties)

Queries = type(
    'Queries',
    tuple(queries_base_classes),
    {}
)
