from django.views.generic import ListView
from django.views.generic.edit import CreateView
from products.models import Product, Category
from products.forms import ProductForm

from django.db.models import Q

class ProductListView(ListView):

    def get_queryset(self):
        if "category" in self.request.GET and self.request.GET.get('category').isdigit():
            return self.filter_by_category(self.request.GET.get('category'))
        if "keyword" in self.request.GET:
            return self.filter_by_keyword(self.request.GET.get('keyword'))
        return Product.objects.all()

    def filter_by_keyword(self, keyword):
        category_title_matches = Category.objects.filter(title__icontains=keyword)
        return Product.objects.filter(Q(title__icontains=keyword) | Q(description__icontains=keyword) | Q(category=category_title_matches)).distinct().all()

    def filter_by_category(self, category_id):
        category = Category.objects.filter(pk=int(category_id))
        return Product.objects.filter(category=category).all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['products'] = list(self.get_queryset())
        # Add in a QuerySet of all the categories
        context['category_list'] = Category.objects.all()
        # Add the create Product form to the QuerySet to be display in a modal
        context['form'] = ProductForm()

        return context


class ProductCreateView(CreateView):

    model = Product
    fields = '__all__'
