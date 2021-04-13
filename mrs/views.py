from rest_framework.response import Response
from rest_framework.views import APIView


class DocsView(APIView):
    """
    RESTFul Documentation for displaying apps on APIRoot
    """
    def get(self, request, *args, **kwargs):
        apidocs = {
            'api/': request.build_absolute_uri('api/'),
        }
        return Response(apidocs)

