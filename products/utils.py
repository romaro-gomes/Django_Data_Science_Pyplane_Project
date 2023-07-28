import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64
from django.contrib.auth.models import User

def get_salesperson_from_id(val):
    salesperson = User.objects.get(id=val)
    return salesperson
    

def get_image():
    # create a bytes buffer for the image the save
    buffer = BytesIO()
    # create the plot with the use od BytesIO object as its 'file'
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    #retreive the entire content of the file
    image_png = buffer.getvalue()
    
    graph =base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    
    # free the memory of the buffer
    buffer.close()
    
    return graph
    

def get_simple_plot(chart_type, *args, **kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10,4))
    x = kwargs.get('x')
    y = kwargs.get('y')
    data =kwargs.get('data')
   
    if chart_type == 'bar':
        title = "Total Price by Day"
        plt.title(title)
        plt.bar(x,y)
        
    elif chart_type == 'line':
        title = "Total Price by Day"
        plt.title(title)
        plt.plot(x,y)
        
    else:
        title = "Total product solded"
        plt.title(title)
        sns.countplot(data=data,hue=data['name'],x=data['name'])
    plt.xticks(rotation=45)
    
    plt.tight_layout()
        
    graph = get_image()
    
    return graph 


