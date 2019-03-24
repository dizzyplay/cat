from cat.models import Cat

def cats(root, info):
    return Cat.objects.all()