from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def home(request):

    user = request.user
    #return HttpResponse(request.user);
    if user.is_authenticated() and not user.is_registered:
        url = reverse('users:register', kwargs={'pk': user.id})
        return HttpResponseRedirect(url)
    else:
        return HttpResponseRedirect(reverse('products:index'))
