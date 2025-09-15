from django.contrib import messages
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from apps.accounts.forms import RegisterModelForm, LoginForm


class RegisterCreateView(CreateView):
    template_name = 'auth/login.html'
    form_class = RegisterModelForm
    success_url = reverse_lazy('pages:home')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        messages.error(self.request, "Successfully registered")
        return super().form_valid(form)



    def form_invalid(self, form):
        errors = []
        for key, value in form.errors.items():
            for error in value:
                messages.error(self.request, error)
        return super().form_invalid(form)



class LoginFormView(FormView):
    template_name = 'auth/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('pages:home')


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


    def form_valid(self, form):
        user = form.cleaned_data.get('user')
        if user:
            login(self.request, user)
        return super().form_valid(form)