from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, loader
from django.core.urlresolvers import reverse

from products.models import Category


def home(request):

    user = request.user
    #return HttpResponse(request.user);
    if user.is_authenticated() and not user.is_registered:
        url = reverse('users:register', kwargs={'pk': user.id})
        return HttpResponseRedirect(url)
    else:
    	category_list = Category.objects.all()
    	context = Context({
    	 	'category_list': category_list
    	 	})
    	template = loader.get_template('home.html')
        return HttpResponse(template.render(context))
