from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CatSerializer
from cat.models import Cat


class CatView(APIView):
    def get(self, request):
        qs = Cat.objects.all()
        serializer = CatSerializer(qs, many=True)
        return Response(serializer.data)


main = CatView.as_view()
