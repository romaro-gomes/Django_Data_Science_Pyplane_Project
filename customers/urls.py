from django.urls import path
from . import views

urlpatterns = [
    path('',views.customer_corr_view,name='customers.main'),
    
]
