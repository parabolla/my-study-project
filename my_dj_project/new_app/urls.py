from django.contrib.auth.decorators import login_required
from django.urls import path

from new_app.views import CustomLoginView, ProfileView, CustomLogoutView, SignupView

app_name = "new_app"

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name='login'),
    path("logout/", CustomLogoutView.as_view(), name='logout'),
    path("signup/", SignupView.as_view(), name='signup'),
    path("profile/<int:user_id>", login_required(ProfileView.as_view()), name='profile'),
]
