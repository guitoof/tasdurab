from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def home(request):

    user = request.user
    if user.is_authenticated() and not user.is_registered:
        return HttpResponseRedirect(reverse('users:create'))
    else:
        return HttpResponseRedirect(reverse('products:index'))
