from django.urls import path
from . import views

urlpatterns = [
    path('',views.chart_select_view,name='main_products_view'),
    path('add/',views.add_purchase_view,name='add_purchase_view'),
    path('sales/',views.sales_dist_view,name='sales_view' )
    
]

