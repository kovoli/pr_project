from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Deal, Category


def home_page(requests):
    deals = Deal.objects.all().select_related('brands')

    return render(requests, 'home_page.html', {'deals': deals})


def deal_detail(requests, slug):
    deal = get_object_or_404(Deal, slug=slug)
    categories = Category.objects.all()

    context = {'deal': deal, 'categories': categories}

    # todo Сделать время обновление скидки
    return render(requests, 'deals/deal_detail.html', context)


def category_deals_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    deals_by_category = Deal.objects.filter(category=category)

    context = {'category': category, 'deals_by_category': deals_by_category}

    render(request, '', context)
