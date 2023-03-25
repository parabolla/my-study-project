from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetView
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.urls import reverse_lazy as _, reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView, UpdateView

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


class ProfileEditView(UpdateView):
    model = CustomerUser
    template_name = 'new_app/edit_profile.html'
    pk_url_kwarg = 'user_id'
    fields = ['avatar', 'first_name', 'last_name', 'email', 'about']

    def get_context_data(self, **kwargs):
        object = self.get_object()
        context = super().get_context_data(**kwargs)
        context['edit'] = f'Edit Profile of {object.username}'
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object != request.user:
            raise PermissionDenied("You are not author")

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        object = self.get_object()
        return reverse('new_app:profile', kwargs={'user_id': object.id})


class CustomPasswordResetView(PasswordResetView):
    success_url = _("new_app:password_reset_done")
    template_name = "new_app/password_reset/password_reset_form.html"
    email_template_name = "new_app/password_reset/password_reset_email.html"
    subject_template_name = "new_app/password_reset/subject_template_name.txt"


class CustomPasswordResetViewDone(PasswordResetDoneView):
    template_name = "new_app/password_reset/password_reset_done.html"


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = _("new_app:password_reset_complete")


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "new_app/password_reset/password_reset_complete.html"
