from django.views.generic import ListView
from django.views.generic.edit import CreateView
from products.models import Product, Category
#from products.forms import ProductForm

class ProductListView(ListView):

    def get_queryset(self):
        """Return all the products"""
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProductListView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the categories
        #context['category_list'] = Category.objects.all()
        #context['pages'] = len(Category.objects.all()) / 20 + 1
        #context['form'] = PresentationForm()
        return context


class ProductCreateView(CreateView):

    model = Product
    fields = '__all__'
