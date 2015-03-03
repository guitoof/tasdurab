from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, loader
from django.core.urlresolvers import reverse


def home(request):

    user = request.user
    #return HttpResponse(request.user);
    if user.is_authenticated() and not user.is_registered:
        url = reverse('users:register', kwargs={'pk': user.id})
        return HttpResponseRedirect(url)
    else:
    	# news_list = News.objects.all()
    	context = Context({
    	# 	'news_list': news_list
    	 	})
    	template = loader.get_template('home.html')
        return HttpResponse(template.render(context))
