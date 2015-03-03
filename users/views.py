from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from users.models import User
from users.forms import UserRegistrationForm

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required

class LoginRequiredMixin(object):

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view, login_url = 'login', redirect_field_name = 'home')


class UserUpdateView(UpdateView):

    model = User
    fields = '__all__'
    form_class = UserRegistrationForm

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['user'] = self.model
        return context

    def get(self, request, *args, **kwargs):
        if request.user.is_registered:
            return HttpResponseRedirect(reverse('home'))
        else:
            return super(UserUpdateView, self).get(**kwargs)


    def post(self, request, *args, **kwargs):

        # get the user instance
        self.object = self.get_object()

        # get the form
        form = self.get_form(self.form_class)


        # validate
        if form.is_valid():
            self.object.is_registered = True
            return self.form_valid(form)
        else:
            return self.form_invalid(form)



class UserDetailView(LoginRequiredMixin, DetailView):

    model = User

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['owner'] = self.object
        # Add in a QuerySet of all the user's products
        context['user_product_list'] = Product.objects.filter( Q(owner=self.object.owner) )
        return context

