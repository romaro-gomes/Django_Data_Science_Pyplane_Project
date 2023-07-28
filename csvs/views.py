from django.shortcuts import render
from django.contrib.auth.models import User
from . import forms
from . import models
from products.models import Product,Purchase
import csv
from django.contrib.auth.decorators import login_required

@login_required
def upload_file_view(request):
    error_message = None
    sucess_message = None
    form = forms.CsvForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = forms.CsvForm()
        
       
    try:
        obj = models.Csv.objects.get(activated=False)
        print(obj)
        obj.activated=True
        obj.save()     
        
        
        with open(obj.file_name.path,'r') as f:
          
            reader = csv.reader(f)
            
                
            for row in reader: 
                print(f'row:{row}')        
                user = User.objects.get(id=row[3])
                print(f'user:{user}')
                product,_ = Product.objects.get_or_create(name=row[0])
                print(f'product:{product}')
                purchase = Purchase.objects.create(
                    product = product,
                    price = int(row[1]),
                    quantity = int(row[2]),
                    salesperson = user,
                        
                    )
                print(f'purchase:{purchase}')
            
            
                         
                    
        
                    
        sucess_message = 'Uploaded sucessfully'
        print(sucess_message)
            
    except:
        error_message ='Ops... Something went wrong'
        print(error_message)
        
    
    context ={
        'form':form,
        'error_message': error_message,
        'sucess_message': sucess_message,
        
    }
        
         
    return render(request, 'csvs/upload.html', context)
