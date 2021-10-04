from django.http.response import HttpResponse, JsonResponse


# Create your views here.

class Clusters(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        return JsonResponse({})
