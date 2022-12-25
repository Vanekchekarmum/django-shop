
from rest_framework.response import Response
from rest_framework.views import APIView

from django.http import HttpResponse


class TestAPIView(APIView):
    def get(self, request, *args, **kwargs):
        data = [{"id": 1, "subject": "english"},{"id": 2,"subject": "math"}]
        return Response(data)

# Compare this snippet from EdPlatform\api\views.py:


def test(request):
    return HttpResponse("Hello World")



