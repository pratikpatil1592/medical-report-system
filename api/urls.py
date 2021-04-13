from .views import APIAppRootView, RegisterAPI, LoginAPI, FileUploadView, PatientListView
from django.urls import path
from knox import views as knox_views


urlpatterns = [
    path('', APIAppRootView.as_view()),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('patient/', PatientListView.as_view(), name='patient-details')
]