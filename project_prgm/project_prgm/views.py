from django.shortcuts import render, redirect


def home_page(request):
    context = {
        'title': 'صفحه اصلی'
    }
    return render(request, 'home_page.html', context)
# footer code behind

def header(request, *args, **kwargs):
    context = {
        'title': 'this is title'
    }
    return render(request, 'shared/Header.html', context)

def footer(request, *args, **kwargs):
    context = {
        "about_us": "این سایت برای راحتی کار کاربران درست شده است که میاید و پول های بازی های محتلف رو خریداری میکند و میفروشد"
    }
    return render(request, 'shared/Footer.html', context)

