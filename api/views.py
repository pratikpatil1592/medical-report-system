from django.contrib.auth import login
from django.conf import settings
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.authtoken.serializers import AuthTokenSerializer
from api.models import CustomUser, FileUpload
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from .serializers import UserSerializer, RegisterSerializer, FileUploadSerializer
from django.db.models import F, Value
from django.db.models.functions import Concat


# API App Root View
class APIAppRootView(APIView):

    def get(self, request, *args, **kwargs):
        apidocs = {
            'register/': request.build_absolute_uri('register/'),
            'login/': request.build_absolute_uri('login/'),
            'logout/': request.build_absolute_uri('logout/'),
            'logoutall/': request.build_absolute_uri('logoutall/'),
            'upload/': request.build_absolute_uri('upload/'),
            'patient/': request.build_absolute_uri('patient/'),
        }
        return Response(apidocs)


# Register API View
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "status": "1",
            "message": "Registration Succeeded",
            "data": {
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "token": AuthToken.objects.create(user)[1]
            }
        })


# Login API View
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        login_data = super(LoginAPI, self).post(request, format=None)
        return Response({
            "status": "1",
            "message": "Login Success",
            "data": login_data.data
        })


# File Upload View
class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = FileUploadSerializer(data=request.data)
        if file_serializer.is_valid() and request.user.is_authenticated:
            file_serializer.save()
            return Response({
                "status": "1",
                "message": "File Uploaded Successfully.",
                "data": file_serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "status": "0",
                "message": "File Upload Failed.",
                "data": file_serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


# Patient Listing View
class PatientListView(APIView):

    def get(self, request):

        get_all_patients = CustomUser.objects.values('patient_name', 'age', 'address', 'phone_number', 'last_login')\
            .annotate(file=Concat(Value('reports_data/'), F('fileupload__file')), filetype=F('fileupload__filetype'))

        return Response({
            "status": "0" if not get_all_patients else "1",
            "message": "Patient Data Not Available." if not get_all_patients else "Patient Data Available.",
            "data": { 
                "patient_list": get_all_patients
            }
        })