from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from . import models
from products.utils import get_image
from django.contrib.auth.decorators import login_required


@login_required
def customer_corr_view(request):
    df = pd.DataFrame(models.Customer.objects.all().values())
    corr = round(df['budget'].corr(df['employment']),2)
    
    plt.switch_backend('Agg')
    
    sns.jointplot(x='budget', y='employment', kind='reg', data=df).set_axis_labels(xlabel='Company budget',ylabel='No of employes')
    graph = get_image()
    
    context ={
        'graphx': graph,
        'corr': corr,
        
    }
    
    return render(request, 'customers/customers.main.html', context)