from django.contrib.auth.models import User
from django.shortcuts import render

from gasell_products.models import Product
from gasell_products.views import my_grouper
from gasell_products_category.models import ProductCategory
from gasell_sliders.models import Slider
from gasell_settings.models import SiteSetting


def home_page(request):
    sliders = Slider.objects.all()
    most_visit_products = Product.objects.order_by('-visit_count').filter(active=True)[:8]
    latest_products = Product.objects.order_by('-id').filter(active=True)[:8]
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    cat_in_product = {}
    for product in products:
        for category in product.categories.all():
            for cat in categories:
                if category.title == cat.title:
                    try:
                        cat_in_product[cat.title].append(product.title)
                    except:
                        cat_in_product.update({cat.title: [product.title]})
    for thing in cat_in_product:
        cat_in_product[thing] = cat_in_product[thing][:4]
    context = {
        'title': 'صفحه اصلی',
        'sliders': sliders,
        'most_visit': my_grouper(4, most_visit_products),
        'latest_products': my_grouper(4, latest_products),
        'categories': categories,
        'cat_in_product': cat_in_product
    }

    return render(request, 'home_page.html', context)


# footer code behind

def header(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()

    context = {
        'setting': site_setting
    }
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        context['user']=user
    return render(request, 'shared/Header.html', context)


def footer(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting
    }
    return render(request, 'shared/Footer.html', context)


def about_page(request):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting
    }
    return render(request, 'about_page.html', context)
