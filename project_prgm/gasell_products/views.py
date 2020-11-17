from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
from gasell_products_category.models import ProductCategory

# Create your views here.


class ProductsList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'محصولات'
        return context

    def get_queryset(self):
        return Product.objects.get_active_products()


class ProductsListByCategory(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 3



    def get_queryset(self):
        print(self.kwargs)
        category_name = self.kwargs['category_name']
        category = ProductCategory.objects.filter(name__iexact=category_name).first()
        global title
        try :
            title = category.title
        except:
            pass
        if category is None:
            raise Http404('صفحه ی مورد نظر یافت نشد')
        return Product.objects.get_products_by_category(category_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = title
        return context

def product_detail(request, *args, **kwargs):
    product_id = kwargs['productId']
    product_name = kwargs['name']

    product = Product.objects.get_by_id(product_id)
    if product is None or not product.active:
        raise Http404('محصول مورد نظر یافت نشد')

    context = {
        'product': product,
        'title': product.title
    }

    return render(request, 'products/product_detail.html', context)

class SearchProductsView(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 3

    def get_queryset(self):
        request = self.request
        print(request.GET)
        query = request.GET.get('q')
        global title
        title = query
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.get_active_products()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = title
        return context



def products_categories_partial(request):
    categories = ProductCategory.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'products/products_categories_partial.html', context)
