from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy as _, reverse
from django.views import View
from django.views.generic import DetailView

from new_app.forms import LoginForm, SignupForm
from new_app.models import CustomerUser


class SignupView(View):
    templates_name = 'new_app/signup.html'
    form = SignupForm

    def get_context_data(self):
        context = {
            'header': 'Signup',
            'form': self.form,
        }
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.templates_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST, request.FILES)
        context = self.get_context_data()
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('post:index'))
        else:
            return render(request, self.templates_name, context)


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
