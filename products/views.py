from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from products.models import Product, Category
from users.models import User
from products.forms import ProductCreateForm

from django.db.models import Q

from django.contrib.auth.decorators import login_required
#
# class LoginRequiredMixin(object):
#     @classmethod
#     def as_view(cls, **initkwargs):
#         view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
#         return login_required(view)

class ProductListView(ListView):

    def get_queryset(self):
        if "category" in self.request.GET and self.request.GET.get('category').isdigit():
            return self.filter_by_category(self.request.GET.get('category'))
        if "keyword" in self.request.GET:
            return self.filter_by_keyword(self.request.GET.get('keyword'))
        return Product.objects.all()

    def filter_by_keyword(self, keyword):
        category_title_matches = Category.objects.filter(title__icontains=keyword)
        owner_name_matches = User.objects.filter(Q(first_name__icontains=keyword) | Q(last_name__icontains=keyword))
        return Product.objects.filter( Q(title__icontains=keyword) | Q(description__icontains=keyword) | Q(category=category_title_matches) | Q(owner=owner_name_matches) ).distinct().all()

    def filter_by_category(self, category_id):
        category = Category.objects.filter(pk=int(category_id))
        return Product.objects.filter(category=category).all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProductListView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the categories
        context['category_list'] = Category.objects.all()
        # Add the create Product form to the QuerySet to be display in a modal
        context['form'] = ProductCreateForm()

        return context

class ProductDetailView(DetailView):

    model = Product

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the related products
        context['related_product_list'] = Product.objects.filter( Q(category=self.object.category) ).exclude( id=self.object.id )
        return context

class ProductCreateView(CreateView):

    model = Product
    fields = '__all__'

    #@login_required
    def dispatch(self, request, *args, **kwargs):        
        return super(ProductCreateView, self).dispatch(request, *args, **kwargs)

    # def form_valid(self, form):
    #     return super(ProductCreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        print 'POST BIATCH'
    #     # get the user instance
    #     self.object = self.get_object()

    #     # get the form
    #     form = self.get_form(self.form_class)

    #     # validate
    #     if form.is_valid():
    #         self.object.owner = request.user
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)
