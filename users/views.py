from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from users.models import User
from users.forms import UserRegistrationForm

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


class UserUpdateView(UpdateView):

    model = User
    fields = '__all__'
    form_class = UserRegistrationForm

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['user'] = self.model
        form = self.get_form(self.form_class)
        form.fields['first_name'].value = 'Michel'
        return context


    # def form_valid(self, form):
    #     form.save()
    #     return super(UserUpdateView, self).form_valid(form)


    def post(self, request, *args, **kwargs):

        # get the user instance
        self.object = self.get_object()

        # get the form
        form = self.get_form(self.form_class)

        #form.fields['first_name'] = self.object.first_name

        # validate
        if form.is_valid():
            self.object.is_registered = True
            return self.form_valid(form)
        else:
            #return HttpResponseRedirect('http://www.google.fr')
            return self.form_invalid(form)


class UserDetailView(DetailView):

    model = User

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['user'] = self.model
        return context
