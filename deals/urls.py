from django.urls import path
from . import views

app_name = 'deals'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('deal/<slug:slug>/', views.deal_detail, name='product_detail'),
    path('category/<slug:slug>/', views.category_deals_list, name='category_deals'),
]
