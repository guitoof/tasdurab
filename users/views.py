from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from users.models import User
from users.forms import UserRegistrationForm


class UserCreateView(CreateView):

    model = User
    fields = '__all__'
    form_class = UserRegistrationForm

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['user'] = self.model
        return context


class UserDetailView(DetailView):

    model = User

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['user'] = self.model
        return context
