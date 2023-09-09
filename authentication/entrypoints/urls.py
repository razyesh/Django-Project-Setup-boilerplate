from django.urls import path
from .views import CustomLoginView

app_name = "auth"

urlpatterns = [path("login/", CustomLoginView.as_view(), name="index")]
