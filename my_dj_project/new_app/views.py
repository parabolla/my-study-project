
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy as _
from django.views.generic import DetailView

from new_app.forms import LoginForm
from new_app.models import CustomerUser


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = "new_app/login.html"
    next_page = _("post:index")
    extra_context = {
        'header': 'Login'
    }
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    next_page = _("post:index")
    http_method_names = ['post', ]


class ProfileView(DetailView):
    model = CustomerUser
    template_name = 'new_app/profile.html'
    pk_url_kwarg = 'user_id'

    def get_context_data(self, **kwargs):
        object = self.get_object()
        context = super().get_context_data(**kwargs)
        context['header'] = f'Profile of {object.username}'
        return context

