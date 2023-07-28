from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from . import models,utils, forms
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@login_required
def sales_dist_view(request):
    error_message = False
    graph=False
    try:
        df=pd.DataFrame(models.Purchase.objects.all().values())
        
        df['salesperson_id'] = df['salesperson_id'].apply(utils.get_salesperson_from_id)
        df.rename({'salesperson_id':'salesperson'},axis=1, inplace=True)
        df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
        
        plt.switch_backend('Agg')
        plt.xticks(rotation=45)
        sns.barplot(x='date',y='total_price', hue='salesperson', data=df)
        plt.tight_layout()
        graph = utils.get_image()
        
       
    except:
        error_message='No Sales'
        
    context ={
            'graph':graph,
            'error_message':error_message
        }
        
    print(df)
    return render(request, 'products/sales.html', context)
    
    
@login_required    
def chart_select_view(request):
    error_message=False
    error_graph = False
    graph = None
    price = None
    df=pd.DataFrame() #Avoid erro im logic
    
    try:
        product_df = pd.DataFrame(models.Product.objects.all().values())
        purchase_df = pd.DataFrame(models.Purchase.objects.all().values())
        product_df['product_id'] = product_df['id']
        
        if purchase_df.shape[0]> 0:
            df = pd.merge(purchase_df,product_df, on='product_id').drop(['id_y','date_y'], axis=1).rename({'id_x':'id', 'date_x':'date'}, axis=1)   
            price = df['price']              
            # Control Form    
            if request.method == 'POST':
                
                chart_type= request.POST['sales']
                date_from = request.POST['date_from']
                date_to=request.POST['date_to']
                
                df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
            
                                
                if chart_type !="":
                    if date_from !='' and date_to !='':
                        df = df[(df['date']>=date_from) & (df['date']<=date_to)]
                        price = df['price']
                        df2=df.groupby('date',as_index=False)['total_price'].agg('sum')
                    #functio to get a graph
                        graph = utils.get_simple_plot(chart_type, x=df2['date'], y=df2['total_price'], data =df)
                              
                    
                
                else:
                    error_graph = 'Please select a chart type to continue'

    except:
        product_df = None
        purchase_df = None
        error_message = 'No records in the database'  
        
    
    df = df.head(10)    
    
    # Varaiables going to html
    context ={
        'price':price,
        "graph": graph,
        'error_message': error_message,
        'error_graph': error_graph,        
        'df':df.to_html(classes='table  table-bordered table-stripped',justify='center')
        #'df':df
    }
        
    return render(request,'products/main.html', context)

@login_required
def add_purchase_view(request):
        
    form = forms.PurchaseForm(request.POST)
    
    if form.is_valid():
        obj = form.save(commit=False)
        obj.salesperson_id = request.user.id
        obj.save()
        
        obj
        form = forms.PurchaseForm()     
   
       
    
        
    context = {
        'form':form,
        
    }
    return render(request,'products/add.html',context)