from django.urls import path
from . import views

urlpatterns = [
    path('user/register',views.UserRegisterApiView.as_view(),name='register')
]
