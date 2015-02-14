from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from users.models import User
from users.forms import UserRegistrationForm

from django.http import HttpResponseRedirect


class UserUpdateView(UpdateView):

    model = User
    fields = '__all__'
    form_class = UserRegistrationForm

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['user'] = self.model
        return context

    def form_invalid(self, form):
        return HttpResponseRedirect("http://www.google.com")#reverse('users:register', kwargs = {'pk': 2}))


    def form_valid(self, form):
        return super(UserUpdateView, self).form_valid(form)


    def post(self, request, *args, **kwargs):

        # get the user instance
        #self.object = self.get_object()

        # get the form
        # form = self.get_form(form_class)
        form = self.get_form(self.form_class)

        # validate
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class UserDetailView(DetailView):

    model = User

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['user'] = self.model
        return context
