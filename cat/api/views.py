from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CatSerializer, CatStatusSerializer
from cat.models import Cat, CatStatus


class CatView(APIView):
    def get(self, request):
        qs = Cat.objects.all()
        serializer = CatSerializer(qs, many=True)
        return Response(serializer.data)


main = CatView.as_view()


class CatStatusView(APIView):
    def get(self, request):
        qs = CatStatus.objects.all()
        serializer = CatStatusSerializer(qs, many=True)
        return Response(serializer.data)


cat_status = CatStatusView.as_view()
